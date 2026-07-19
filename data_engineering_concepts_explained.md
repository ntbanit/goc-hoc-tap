# Data Engineering Concepts Explained Simply (with examples & code)

---

## 1. Spark Shuffle, AQE, Broadcast Join — explained like you're new

**Shuffle — the expensive part**
Imagine you have 8 workers, and each worker holds a random pile of receipts. You want to group all receipts by `customer_id`. Since receipt #123 for "Alice" might be sitting on Worker 3 while another Alice receipt is on Worker 7, Spark has to **physically move data across the network** so all of Alice's receipts land on the same worker. That network movement + disk write/read is a **shuffle** — it's slow and is the #1 cause of slow Spark jobs.

Any `groupBy`, `join`, `distinct`, or `repartition` can trigger a shuffle.

**Broadcast Join — avoid the shuffle entirely**
If one side of a join is small (say, a 5MB `countries` lookup table), instead of shuffling the huge table around, Spark just **copies the small table to every worker's memory**. Now each worker can do the join locally — no shuffle needed for the big table at all.

```python
from pyspark.sql.functions import broadcast

# orders is 200GB, countries is 5MB
result = orders.join(broadcast(countries), on="country_code", how="left")
```

Spark auto-broadcasts tables under `spark.sql.autoBroadcastJoinThreshold` (default 10MB), but you can force it with the hint above if Spark's size estimate is wrong.

**AQE (Adaptive Query Execution) — Spark adjusts its plan mid-flight**
Normally Spark plans the whole query upfront based on *estimated* data sizes. But estimates are often wrong (especially after filters). AQE lets Spark **look at actual data sizes after each stage** and re-optimize — e.g., switching a shuffle join to a broadcast join if it turns out one side became small after filtering, or splitting a skewed partition automatically.

```python
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
```

**Quick analogy summary:**
| Concept | Analogy |
|---|---|
| Shuffle | Moving boxes between warehouses to regroup them |
| Broadcast join | Photocopying a small phonebook and giving everyone a copy instead of moving people around |
| AQE | Spark re-checking the map mid-road-trip instead of blindly following the original plan |

---

## 2. Spark Executors, Fact vs Dimension Tables, "Spilling Safely"

**Executor** = a worker process (JVM) running on a machine in your cluster. Each executor has a fixed slice of CPU cores and memory (e.g., 4 cores, 16GB). Your job is split into tasks, and tasks run inside executors.

**Fact (transaction) table vs Dimension table** — classic warehousing terms:
- **Fact/transaction table**: the big one, records *events* — e.g., `orders` (200M rows, grows every day: order_id, customer_id, product_id, amount, timestamp).
- **Dimension table**: the small, descriptive one — e.g., `products` (5,000 rows: product_id, name, category, price). Rarely changes.

```python
# Bad: shuffle join, both sides get shuffled across the network
result = orders.join(products, "product_id")

# Good: since products is small, broadcast it — no shuffle for the 200M-row table
result = orders.join(broadcast(products), "product_id")
```

**"Spilling safely" — what it means**
When a task processes more data than fits in its executor's memory, Spark can **spill** — write the overflow to local disk temporarily instead of crashing. It's slower (disk I/O), but the job *completes* instead of throwing `OutOfMemoryError`.

You control this via **storage level** when caching:
```python
from pyspark import StorageLevel

# MEMORY_ONLY: fast, but crashes/recomputes if it doesn't fit
df.persist(StorageLevel.MEMORY_ONLY)

# MEMORY_AND_DISK: tries memory first, spills to disk instead of failing
df.persist(StorageLevel.MEMORY_AND_DISK)
```
Think of it like a desk (memory) vs a filing cabinet (disk). If your desk is full, you don't throw the papers away (crash) — you put the overflow in the cabinet (spill) and keep working, just a bit slower.

---

## 3. Why Plain Parquet Backfills Cause Read Inconsistency, and How Iceberg/Catalogs Solve It

**The core problem**
A plain Parquet "table" in S3 is really just **a folder of files** — there's no single source of truth for "what files currently make up this table." A query engine (Athena/Spark) usually just lists all files under the folder/partition path at query time.

Now imagine this backfill scenario:
1. Analyst is running a query on `s3://bucket/orders/date=2026-07-15/` at 10:00:00.
2. At 10:00:01, your backfill job **deletes** the old files in that partition and starts writing new corrected ones.
3. The analyst's query, which is mid-read, now sees a **mix of some deleted-and-gone files and some new half-written files** — or gets errors, or gets duplicate/missing rows. There's no atomicity.

This is exactly the problem **Iceberg (and Delta Lake, Hudi)** were built to solve.

**How Iceberg fixes it**
Iceberg keeps a **metadata log of snapshots**. A "table" isn't "everything in this folder" — it's "exactly the files listed in snapshot #47." When you overwrite a partition:
1. Iceberg writes the *new* Parquet files (old ones untouched).
2. Iceberg atomically publishes a new snapshot that points to the new files instead of the old ones — this is a single metadata pointer swap, similar to a Git commit.
3. Any query that started before the swap keeps reading the *old* snapshot consistently (nothing changes underneath it). Any query starting after sees the new snapshot. No mixed/partial reads, ever.

```sql
-- Overwrite one partition atomically, in Iceberg
INSERT OVERWRITE TABLE orders
PARTITION (date = '2026-07-15')
SELECT * FROM orders_corrected_day15;
```

**Hive Metastore vs Iceberg on schema evolution**
- **Hive Metastore** just stores "table X has these columns, and lives at this S3 path, partitioned like this." If you add a column, or reorder columns, Hive matches columns to Parquet files **by position/name convention**, which breaks easily (e.g., old files don't have the new column, or column order changed causes wrong values to line up).
- **Iceberg** assigns every column a permanent internal **field ID** at creation time, not a position. Even if you add, drop, rename, or reorder columns later, Iceberg matches columns by ID, not position — so old Parquet files (which don't have field X) simply return `null` for that field, and reordering never scrambles data. This is what "safe schema evolution" really means.

```sql
-- Safe with Iceberg — old files unaffected, new files get the new column
ALTER TABLE orders ADD COLUMN discount_pct DOUBLE;
ALTER TABLE orders RENAME COLUMN amount TO order_amount;
```

**Multi-day correction scenario (your example)**
You're back from holiday on Day 5 and discover Day 1's data was wrong — and because Day 1 was wrong, every day since (2, 3, 4, 5) that depended on cumulative/rolling calculations is also wrong.

Practical fix-forward approach:
```python
# Step 1: Fix Day 1 at the source
corrected_day1 = fix_source_data(raw_day1)
corrected_day1.write.mode("overwrite") \
    .option("replaceWhere", "date = '2026-07-01'") \
    .saveAsTable("raw_orders")   # or use Iceberg's partition overwrite (SQL above)

# Step 2: Re-run the pipeline for Day 1 through Day 5, in order,
# since each day's aggregate/rolling numbers depend on the previous day
for d in ["2026-07-01","2026-07-02","2026-07-03","2026-07-04","2026-07-05"]:
    run_pipeline(run_date=d)   # your existing scheduled job, re-triggered manually
```
Key ideas:
- Use **Iceberg's atomic partition overwrite** so each day's fix doesn't corrupt readers mid-fix.
- Because of dependency ordering (rolling 7-day averages, cumulative totals, etc.), you must **re-process in chronological order**, not fix all 5 days in parallel.
- If your orchestrator is Airflow, this is usually just **backfilling a date range**: `airflow dags backfill -s 2026-07-01 -e 2026-07-05 my_dag`.
- Communicate to stakeholders that historical dashboard numbers for that range will shift — this is a common and expected part of data correction, not a failure.

---

## 4. Simulated Debugging Session — Revenue 15% Too Low

**Scenario:** Dashboard shows today's revenue is 15% lower than expected. Pipeline: `ingest → clean → dedupe → join(customers) → aggregate → load`.

**Step 1 — Confirm the discrepancy is real, not a dashboard bug**
```sql
-- Query the final aggregate table directly, bypass the dashboard/BI tool
SELECT SUM(revenue) AS total_revenue, COUNT(*) AS row_count
FROM analytics.daily_revenue_agg
WHERE date = '2026-07-19';
```
Compare against yesterday and last week same-day:
```sql
SELECT date, SUM(revenue) AS total_revenue, COUNT(*) AS row_count
FROM analytics.daily_revenue_agg
WHERE date BETWEEN '2026-07-12' AND '2026-07-19'
GROUP BY date
ORDER BY date;
```
→ Confirms today really is ~15% lower, not just a display issue.

**Step 2 — Bisect the pipeline: check row counts at each stage's output**
```sql
-- Raw ingested rows
SELECT COUNT(*) FROM raw.orders_ingested WHERE date = '2026-07-19';

-- After cleaning
SELECT COUNT(*) FROM staging.orders_cleaned WHERE date = '2026-07-19';

-- After dedupe
SELECT COUNT(*) FROM staging.orders_deduped WHERE date = '2026-07-19';

-- After join with customers
SELECT COUNT(*) FROM staging.orders_joined WHERE date = '2026-07-19';
```
Suppose results are:
```
raw_ingested:     500,000
cleaned:          498,200
deduped:          497,900
joined:           423,100   <-- big drop here!
```
→ The **join stage** dropped ~75,000 rows (~15%). Root cause is likely here.

**Step 3 — Inspect the join for the cause**
```sql
-- Check if it's an inner join silently dropping unmatched customers
SELECT o.customer_id
FROM staging.orders_deduped o
LEFT JOIN dim.customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL
LIMIT 20;
```
Result: 75,000 orders have `customer_id` values that don't exist in `dim.customers`. Checking `dim.customers` load logs shows the customer dimension refresh **failed or ran late today**, so it's missing today's newly-registered customers, and the pipeline used an `INNER JOIN` which silently drops any order whose customer isn't found yet.

**Step 4 — Fix**
- Immediate: switch to `LEFT JOIN` (or delay the orders job until the customer dimension is confirmed refreshed) so new customers aren't dropped.
- Root cause fix: alert/fail the pipeline if `dim.customers` refresh didn't complete before the orders join runs (add a dependency check).
- Backfill: re-run today's aggregate after the customer dimension is fixed.

This is the general debugging pattern: **confirm → bisect by counting at each stage → inspect the specific stage → find root cause → fix + prevent recurrence.**

---

## 5. CDC (Change Data Capture) Replication to a Data Lake/Warehouse

**What CDC is, in plain terms**
Instead of running `SELECT * FROM orders` against your production MySQL every hour (which is slow and adds load to a live transactional database), CDC **reads MySQL's internal transaction log (the binlog)** — the same log MySQL uses for replication — and streams out every INSERT/UPDATE/DELETE as an event, in near real-time, without ever querying the table directly.

**Why it matters:** zero extra load on production DB, near-real-time freshness, and you capture *deletes* and *updates* too (a plain `SELECT` snapshot can't tell you a row was deleted).

**Typical stack: Debezium + Kafka + S3**
```
MySQL (binlog enabled)
   │
   ▼
Debezium (Kafka Connect source connector) — reads binlog, emits change events
   │
   ▼
Kafka topic: mysql.sales.orders  (each message = one row change: insert/update/delete)
   │
   ▼
Kafka Connect S3 Sink connector (or Spark Structured Streaming consumer)
   │
   ▼
S3 (raw change-event Parquet files) → Iceberg MERGE to build up-to-date table
```

Example Debezium connector config (conceptual):
```json
{
  "name": "mysql-orders-connector",
  "config": {
    "connector.class": "io.debezium.connector.mysql.MySqlConnector",
    "database.hostname": "prod-mysql.internal",
    "database.user": "cdc_reader",
    "database.server.name": "salesdb",
    "table.include.list": "sales.orders",
    "snapshot.mode": "initial"
  }
}
```

Applying the change stream to your lake table (merge upserts/deletes):
```python
# Simplified: merge a batch of CDC events into an Iceberg table
changes_df.createOrReplaceTempView("cdc_batch")

spark.sql("""
MERGE INTO lake.orders t
USING cdc_batch s
ON t.order_id = s.order_id
WHEN MATCHED AND s.op = 'd' THEN DELETE
WHEN MATCHED AND s.op = 'u' THEN UPDATE SET *
WHEN NOT MATCHED AND s.op = 'c' THEN INSERT *
""")
```
(`op` = c/u/d for create/update/delete, standard Debezium event field.)

**AWS-managed alternative:** AWS DMS (Database Migration Service) does the same binlog-reading job without you running Kafka/Debezium yourself — simpler to operate, less flexible.

---

## 6. Spark Compaction, and a Low-Cost On-Prem Stack

**The small-file problem**
Streaming/frequent-batch jobs tend to write many tiny files (e.g., 1,000 files of 2MB each instead of 10 files of 200MB). Small files are bad because:
- Every file read has fixed overhead (open connection, read footer/metadata) — thousands of tiny reads is much slower than a few big reads.
- The catalog (Hive Metastore/Iceberg metadata) also grows huge tracking millions of tiny files.

**Compaction = merging small files into fewer, larger ones**
```python
# Plain Spark: read a partition, rewrite it with fewer, bigger files
df = spark.read.parquet("s3://bucket/orders/date=2026-07-19/")
df.repartition(4) \
  .write.mode("overwrite") \
  .parquet("s3://bucket/orders_compacted/date=2026-07-19/")
```

If using Iceberg, it has a built-in compaction procedure that does this safely (atomic, no downtime for readers):
```sql
CALL catalog.system.rewrite_data_files(
  table => 'lake.orders',
  options => map('target-file-size-bytes','268435456')  -- 256MB target
);
```
Run this as a scheduled job (e.g., nightly) — not on every write, since compaction itself has a cost.

**On-Prem, cost-minimized stack (no AWS bill)**
| Layer | Tool | Why |
|---|---|---|
| Object storage | **MinIO** | S3-compatible API, runs on your own commodity hardware/disks, free & open source |
| Table format | **Apache Iceberg** | ACID, compaction, schema evolution — same as cloud, storage-engine agnostic |
| Catalog | **Hive Metastore** (or Iceberg's REST/JDBC catalog) | Free, self-hosted, well supported |
| Compute | **Apache Spark** (standalone or on Kubernetes via a self-managed k8s cluster) | Free, avoids paying for EMR/Databricks |
| Orchestration | **Apache Airflow** (self-hosted, e.g., on a small VM or k8s) | Free, avoids paying for MWAA |
| Monitoring | **Prometheus + Grafana** | Free, standard for on-prem metrics/alerting |

This mirrors the AWS stack (S3→MinIO, Glue Catalog→Hive Metastore, EMR→self-managed Spark, MWAA→self-hosted Airflow) but trades **operational effort (you patch/scale/monitor it yourself)** for **lower direct cost** — the right call mainly when you have steady, predictable workloads and existing hardware/ops capacity, not spiky demand.

---

## 7. Schema Evolution Checks & Data Validation Gates — Can Unit Tests Cover This Fully?

**Short answer: No — unit tests alone can't fully cover this.** Here's why, and what fills the gap.

**Schema evolution check example**
A simple CI check comparing the new pipeline's output schema against the last known-good schema:
```python
def check_schema_compatible(old_schema, new_schema):
    old_fields = {f.name: f.dataType for f in old_schema.fields}
    new_fields = {f.name: f.dataType for f in new_schema.fields}

    removed = set(old_fields) - set(new_fields)
    if removed:
        raise ValueError(f"Breaking change: columns removed: {removed}")

    for col, dtype in old_fields.items():
        if col in new_fields and new_fields[col] != dtype:
            raise ValueError(f"Breaking change: {col} type changed "
                              f"from {dtype} to {new_fields[col]}")
    print("Schema check passed — safe to deploy")

check_schema_compatible(previous_run_df.schema, new_run_df.schema)
```

**Data validation gate example (using Great Expectations style logic)**
```python
def validate_output(df):
    total = df.count()
    nulls = df.filter(df.revenue.isNull()).count()
    negative = df.filter(df.revenue < 0).count()

    assert total > 0, "Output is empty!"
    assert nulls / total < 0.01, f"Too many nulls: {nulls}/{total}"
    assert negative == 0, f"Found {negative} negative revenue rows"

    print(f"Validation passed: {total} rows, {nulls} nulls, {negative} negative")

validate_output(pipeline_output_df)
```
This would run as a **gate step in CI/CD after the job runs on staging data**, blocking promotion to production if it fails.

**Why unit tests alone aren't enough:**
- **Unit tests** check your *code logic* against small, hand-crafted sample data (e.g., "does my `dedupe()` function correctly drop duplicate rows given this 5-row fixture?"). They're great for logic correctness but they **can't catch problems that only appear in real data** — e.g., a new NULL pattern from upstream, a currency field suddenly containing strings like `"1,200.50 USD"`, or a genuine volume/skew issue.
- **Schema/data validation gates** run against **real (or realistic staging) data volumes** and catch the things unit tests structurally can't: actual null rates, actual duplicate rates, actual schema drift from an upstream system you don't control, and actual data skew/volume issues.
- **Integration tests** sit in between — running the full pipeline end-to-end on a small but *real-shaped* dataset to catch wiring issues (e.g., a broken join key) that isolated unit tests miss.

**Rule of thumb:** unit tests catch "did I write the logic right"; schema/data validation gates catch "is the *world* still behaving the way my logic assumes." You need both — they cover different failure classes.

---

## 8. Data Leakage / Timing Issues as Root Causes — Concrete Examples

These are subtle bugs where **the pipeline logic is completely correct**, but the *input data itself* silently changed in a way that skews results. Three common real examples:

**a) Tracking pixel change**
A marketing team updates the website, and in the process the analytics tracking pixel (the tiny script that fires an event on page load) gets moved to load *after* a slow banner ad instead of immediately. Result: on slow connections, the pixel never fires before the user leaves. Your "conversion rate" metric drops — not because fewer people converted, but because **fewer events are being recorded at all**. 
→ How you'd catch it: compare *raw event volume* trends (not just the rate) — a drop in total tracked sessions alongside a stable conversion count points to a tracking issue, not a real behavior change.

**b) Broken redirect**
An old marketing campaign URL (`/promo/summer-sale`) is supposed to redirect to `/products/summer-collection`, and your analytics tags the click on the *landing* page. Someone changes the redirect target during a site refactor, and now that link either 404s or lands on a different (untagged) page. Your campaign's attributed traffic silently drops to zero, even though the actual ad spend and impressions didn't change.
→ How you'd catch it: monitor for 404 rate spikes, and periodically smoke-test key campaign URLs as part of monitoring, not just trust the analytics numbers in isolation.

**c) Schema change that silently nulls a field**
An upstream mobile app team renames a field in their event payload from `user_id` to `userId` (camelCase migration). Your ingestion pipeline was written expecting `user_id`, so instead of erroring, it just doesn't find the field and inserts `NULL` for every row going forward — the pipeline "succeeds," row counts look normal, but a downstream join on `user_id` now matches nothing for new data.
→ How you'd catch it: null-rate monitoring per column (see Q4/Q7) — a column that was reliably 0% null suddenly jumping to 100% null is a near-certain schema drift signal, and should page someone, not just silently pass.

**The common thread:** these bugs don't throw errors — the pipeline runs "successfully." That's exactly why **data quality monitoring (null rates, volume trends, distribution checks)** matters as much as pipeline success/failure monitoring. A green checkmark on your job doesn't mean the *numbers* are right.

---

## 9. SLA (Service Level Agreement) in a Data Engineering Context

**In plain terms:** an SLA is a **promise, with a measurable number attached**, about when or how reliably your data will be ready. It turns "the pipeline should be fast" (vague, unmeasurable) into "the pipeline must complete by 7:00 AM UTC on 99% of days" (specific, checkable).

**Typical components of a data pipeline SLA:**
- **Freshness/timeliness**: "Daily revenue data must be available by 7:00 AM UTC."
- **Completeness**: "99.9% of source records must be present in the output" (allows for some acceptable tiny loss, e.g., known late-arriving data).
- **Correctness**: "Aggregate totals must match source system totals within 0.1%."
- **Availability**: "The dataset/table must be queryable 99.5% of the time during business hours."

**Example, made concrete:**
```
Pipeline: daily_revenue_agg
SLA: Available by 07:00 UTC, 99% of business days per month
Owner: data-eng-team
Escalation: page on-call if not complete by 06:45 UTC (15-min buffer before breach)
```

**How you'd actually implement/monitor an SLA:**
```python
# Airflow example: SLA on a task
from airflow.operators.python import PythonOperator
from datetime import timedelta

task = PythonOperator(
    task_id="build_daily_revenue_agg",
    python_callable=build_agg,
    sla=timedelta(hours=7),   # must finish within 7 hrs of DAG start
    dag=dag,
)
# Airflow automatically emails/alerts if this SLA is missed
```
The key mindset: an SLA isn't just a target you hope to hit — it's something you **actively monitor and alert on before it's breached** (e.g., page at 6:45 if not done, rather than stakeholders discovering it's late at 9:00).

---

## 10. Yes — "Pre-Deploy Validation Gate" Is Solved With CI/CD

You're right to connect these. A **pre-deploy validation gate** is simply a **required step in your CI/CD pipeline that must pass before a deployment is allowed to proceed** — same mechanism as running unit tests before merge, just extended to run data checks before promoting a pipeline to production.

**Example: GitHub Actions workflow**
```yaml
name: Deploy Data Pipeline

on:
  push:
    branches: [main]

jobs:
  test-and-validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run unit tests
        run: pytest tests/unit/

      - name: Run pipeline against staging dataset
        run: python run_pipeline.py --env staging --date 2026-07-18

      - name: Run schema + data validation gate
        run: python validate_output.py --env staging
        # This script runs the checks from Q7 above.
        # If it exits non-zero, the workflow stops here — deploy never happens.

  deploy-to-prod:
    needs: test-and-validate   # only runs if validation gate passed
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to production
        run: ./deploy.sh prod
```

**Why this matters:** without this gate, a code change could pass all unit tests (which only check logic on toy data) but still break in production because of a real-data issue — e.g., an upstream schema change, a null spike, or unexpectedly negative values. The validation gate is what **catches that class of bug before it reaches production**, by running the actual pipeline against real/staging data as part of the deploy process itself, and refusing to promote the deploy if the output looks wrong.

This directly ties back to the CI/CD incident from earlier ("manual SSH deploys causing partial-apply incidents") — a proper CI/CD pipeline with this gate would have caught the bad deploy automatically, instead of a human discovering it in production.
