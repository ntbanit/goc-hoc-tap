import os
import resource

# Check current limits
soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
print(f"Soft limit: {soft}, Hard limit: {hard}")

# Try to open many files
open_files = []
try:
    for i in range(10000):
        f = open(f"temp_{i}.txt", "w")
        open_files.append(f)
        if i % 100 == 0:
            print(f"Opened {i} files...")
except OSError as e:
    print(f"\n❌ Error after opening {len(open_files)} files: {e}")
finally:
    # Clean up
    for f in open_files:
        f.close()