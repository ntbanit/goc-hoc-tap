# Data Engineer Interview Prep — Scenario-Based Q&A

Based on JD: Python (3+ yrs), data pipelines, data analytics tools, storage formats (Parquet/CSV/Iceberg), memory optimization, pipeline observability, Spark, AWS, MySQL/RDBMS, Git/Jira/Confluence, CI/CD.

---

## 1. Data Skew in Spark
**Context:** You partition sales data by `date`. Today a major store ran a 30% discount campaign, so one partition (today's date) has 10x the volume of any other partition. Your Spark job that used to finish in 20 minutes is now taking 3 hours, and you can see in the Spark UI that one task is running far longer than the rest.

**What's happening & how do you fix it?**
- Diagnose first: check Spark UI stage view for skewed task duration/shuffle read size; confirm it's a single key (today's date, or a specific store_id) dominating a shuffle stage (groupBy/join).
- Fixes:
  - **Salting**: add a random suffix to the skewed key, split the hot partition into N sub-keys, aggregate, then combine.
  - **AQE (Adaptive Query Execution)**: enable `spark.sql.adaptive.enabled` and `spark.sql.adaptive.skewJoin.enabled` so Spark auto-splits skewed partitions at runtime.
  - **Repartition by a higher-cardinality key** (e.g., `date + store_id`) instead of `date` alone.
  - For skewed joins: broadcast the small side if one side is small enough (`broadcast()` hint), avoiding shuffle entirely.
- Longer-term: reconsider partitioning strategy — partition by `date` + a hash bucket of `store_id`, or use dynamic partitioning to avoid single-day hot spots.

---

## 2. Memory Optimization — OOM on a Large Join
**Context:** A daily ETL job joins a 200GB transactions table with a 5GB dimension table in Spark on a cluster with limited executor memory. The job used to run fine, but after data volume grew, executors are dying with `OutOfMemoryError`.

**How do you approach this?**
- Check if the smaller (5GB) table can be **broadcast** instead of shuffle-joined — eliminates shuffle for the large table.
- Review executor memory config: `spark.executor.memory`, `spark.executor.memoryOverhead`, and whether too few partitions are causing each task to hold too much data in memory (increase `spark.sql.shuffle.partitions`).
- Check for **data skew** (see Q1) as a common OOM cause — a few partitions holding disproportionate data.
- Use **columnar pruning** — only select needed columns before the join, not `SELECT *`.
- Consider **caching/persisting** intermediate results with the right storage level (`MEMORY_AND_DISK`) instead of `MEMORY_ONLY` to spill safely instead of crashing.
- If using Pandas anywhere in the pipeline, check for unnecessary `.collect()` calls pulling full Spark DataFrames into driver memory — this is a very common root cause.

---

## 3. Choosing a Storage Format (Parquet vs CSV vs Iceberg)
**Context:** A new pipeline ingests raw clickstream data (append-only, ~50M rows/day) that downstream analysts query with ad-hoc SQL, and the data occasionally needs backfills/corrections for specific days.

**Which format would you choose and why?**
- **Raw landing zone**: CSV or JSON might come in as-is from source, but you'd convert immediately to **Parquet** for columnar compression and predicate pushdown, since analysts run ad-hoc filtered queries (huge read speed/cost improvement vs CSV).
- **Table format**: Given the need for **backfills/corrections**, use **Apache Iceberg** on top of Parquet — it gives you ACID transactions, time travel, and safe overwrite of specific partitions without breaking readers mid-query (unlike raw Parquet files in S3, where a backfill can cause read inconsistency).
- Trade-off to mention: Iceberg adds metadata management overhead and requires a catalog (Glue/Hive), but it solves the "in-place correction" and schema evolution problems CSV/plain Parquet can't handle safely.

---

## 4. Pipeline Observability & Traceability
**Context:** A downstream dashboard shows revenue numbers that look 15% too low. Nobody can immediately tell which of the 6 pipeline stages (ingest → clean → dedupe → join → aggregate → load) introduced the discrepancy, or when.

**How would you have designed the pipeline to catch this faster, and how do you debug it now?**
- Debugging now: bisect — check row counts and checksums/aggregates at each stage's output (e.g., a lightweight "stage validation" query comparing row count and sum(revenue) in vs out) to isolate which stage dropped/altered data.
- Prevention going forward:
  - **Row-count and null-rate metrics** emitted at each stage (to CloudWatch, Datadog, or a metrics table), so a sudden drop is visible immediately.
  - **Data lineage tagging** — attach a pipeline run ID / batch ID to every record so any row can be traced back to its source ingestion run.
  - **Automated data quality checks** (e.g., Great Expectations, or custom assertions) run between stages: schema checks, null thresholds, row-count deltas vs previous run.
  - **Structured logging** with consistent job/run IDs so logs across stages can be correlated in one query.
  - Alerting thresholds (e.g., if row count deviates >X% from a 7-day moving average, alert before the data reaches the dashboard).

---

## 5. RDBMS / MySQL — Slow Query in Production
**Context:** A MySQL query that powers a nightly extraction job (`SELECT * FROM orders WHERE created_at BETWEEN ... AND status = 'completed'`) used to take 2 minutes, now takes 40 minutes as the `orders` table has grown to 500M rows.

**How do you diagnose and fix this?**
- Run `EXPLAIN` on the query to see if it's doing a full table scan instead of using an index.
- Check whether there's a **composite index** on `(created_at, status)` — a single index on `created_at` alone won't help much if `status` filtering still scans a huge range.
- Consider **table partitioning** by date range in MySQL if the table is queried mostly by date.
- Avoid `SELECT *` — select only needed columns, especially if there are large TEXT/BLOB columns adding I/O overhead.
- Longer term: if this is a recurring analytics extraction, consider moving it off the transactional DB entirely (e.g., **CDC replication** to a data lake/warehouse via Debezium or AWS DMS) so heavy analytical queries don't compete with production OLTP load.

---

## 6. Designing a Pipeline End-to-End (AWS)
**Context:** You're asked to design a pipeline that ingests IoT sensor data (~1M events/minute) from Kafka, needs to be queryable by analysts within 15 minutes of arrival, and must be cost-efficient to store for 2 years.

**Walk through your design.**
- **Ingestion**: Kafka → **AWS Kinesis Firehose or Spark Structured Streaming** on EMR, batching small windows (e.g., 1-5 min micro-batches) to avoid tiny-file problems.
- **Storage**: land raw data in **S3** partitioned by ingestion date/hour, written as **Parquet** for compression and low storage cost; use **Iceberg/Glue Catalog** for schema management and to support compaction jobs.
- **Compaction**: since streaming writes create many small files, run a periodic compaction job (Spark or Iceberg's built-in compaction) to merge them — otherwise query performance degrades badly over time.
- **Compute for analysts**: expose via **Athena** (serverless, pay-per-query) on top of the Iceberg tables for the 15-min-SLA queries; use EMR/Spark for heavier scheduled aggregation jobs.
- **Cost efficiency over 2 years**: use S3 lifecycle policies to transition older partitions to cheaper storage tiers (S3 Infrequent Access/Glacier) once they're rarely queried, and apply Iceberg's data retention/expiration for old snapshots.
- **Orchestration**: Airflow or Step Functions to manage the batch aggregation and compaction DAGs, with CloudWatch alarms on failures/latency SLA breaches.

---

## 7. CI/CD for Data Pipelines
**Context:** Your team currently deploys pipeline code changes by manually SSH-ing into a server and running `git pull`, which has caused at least two production incidents from partially-applied changes.

**How would you set up CI/CD for this, and what data-specific challenges does it need to handle beyond typical app CI/CD?**
- Standard CI: on PR, run linting, unit tests, and integration tests against a small sample/mock dataset — never against production data.
- CD: package the pipeline (Docker image or versioned wheel/jar) and deploy through a pipeline (GitHub Actions/Jenkins → deploy to EMR/ECS/Airflow) rather than manual SSH, with rollback capability (keep last N versions deployable).
- **Data-specific challenges**:
  - **Schema compatibility tests** — verify new code doesn't break contracts with downstream consumers (schema evolution checks).
  - **Backward-compatible deploys** — since pipelines are often stateful (checkpoints, offsets), a bad deploy can corrupt in-flight state; need blue/green or canary strategies for streaming jobs specifically.
  - **Data validation gates** — a deploy step that runs the new pipeline version against a staging dataset and compares output against expected/previous output before promoting to prod.
- Use Jira to track the change, link the PR, and require a code review + passing checks before merge; document the deployment runbook in Confluence.

---

## 8. Analyzing Data — Python vs Spark, Choosing the Right Tool
**Context:** An analyst asks you to investigate why a specific customer segment's conversion rate dropped last week. The relevant dataset is 2GB for that segment, but sits inside a 3TB overall events table in S3.

**How do you approach this — Pandas or Spark, and why?**
- First, filter down early: use Spark (or Athena/SQL) to push the filter (`WHERE segment = X AND date >= ...`) down at the storage layer using partition pruning — never read all 3TB into any tool.
- Once filtered to ~2GB, that comfortably fits in memory on a single machine — switch to **Pandas** for the actual exploratory analysis (faster iteration, no cluster overhead, richer plotting/statistics ecosystem).
- General principle to communicate in the answer: use **Spark/SQL for the "reduce" step** (filtering, aggregating, joining at scale) and **Pandas for the "explore" step** once data is small enough — don't use Spark for everything by default, since its overhead isn't worth it for small filtered datasets, and don't try to force Pandas on data that doesn't fit in memory.
- Mention checking for **data leakage/timing issues** as a real root cause candidate (e.g., a tracking pixel change, a broken redirect, a schema change that silently nulled a field) rather than jumping straight to "the numbers are just down."

---

## 9. Data Analytics Tooling — Building Visibility for Non-Engineers
**Context:** Business stakeholders keep pinging you on Slack asking "is today's data ready yet?" because they have no visibility into pipeline status.

**How do you solve this using the tools available to you (Git/Jira/Confluence-adjacent, or data tools)?**
- Build a lightweight **status dashboard** (could be a simple table in a BI tool like QuickSight/Looker/Metabase, or even a Confluence page auto-updated via API) showing last successful run time, row counts, and SLA status per pipeline.
- Emit pipeline completion events to a Slack channel automatically (via Airflow callbacks or a Lambda on job completion) instead of relying on people asking.
- Document each pipeline's **SLA, owner, and schedule** in Confluence so stakeholders can self-serve the answer to "when should this be ready."
- Use Jira to track recurring pipeline incidents/delays as tickets, so patterns (e.g., "this job is late every Monday") become visible and prioritized for a real fix rather than staying a recurring interruption.

---

## 10. Debugging a Broken Production Pipeline Under Time Pressure
**Context:** It's 7 AM. The nightly pipeline that populates the executive dashboard failed at 3 AM. The data is due to leadership at 9 AM. You just got paged.

**Walk through what you actually do in the first 30 minutes.**
- **Triage first, don't fix blindly**: pull the job logs/Spark UI or Airflow task logs for the failed run to identify the actual error (OOM? schema mismatch from an upstream source change? a null spike causing a join to explode? a MySQL connection timeout?).
- Check whether this is a **new failure mode** or a **known flaky issue** (check Jira/runbook for past incidents first — don't reinvent the diagnosis).
- Decide fast: is this fixable in time, or do you need a **fallback** (e.g., serve yesterday's data with a note, or a partial/best-effort dataset) to hit the 9 AM deadline while the real fix happens after?
- Communicate early — tell stakeholders by 7:30-7:45 whether data will be on time, late, or partial, rather than going silent until 9 AM.
- After resolving: write a short **postmortem** (root cause, fix, prevention) and add/improve a monitoring check so this failure mode pages earlier next time (e.g., before 3 AM if it's a predictable upstream dependency issue) or gets caught by a pre-deploy validation gate.

---

### Tips for using this guide
- For each answer, be ready to go one level deeper if asked "how would you actually implement that in code/config" — interviewers often follow up on the Spark config names, SQL, or AWS service specifics.
- Practice tying each answer back to a **real project you've worked on**, even if you have to adapt these scenarios to your own experience.
