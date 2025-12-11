import os
import time

def buffered_write():
    # 'w' is write text mode. The default buffering value (omitted or set to a positive int)
    # uses a large internal buffer (e.g., 4096 or 8192 bytes).
    try:
        with open("buffered_output.txt", "w") as f:
            start_time = time.time()
            for i in range(100000):
                # The data is accumulated in a fast memory buffer.
                # Only when the buffer is full, one expensive OS write occurs.
                f.write("data")
            # The buffer is flushed (written to disk) automatically upon 'with' exit.
            end_time = time.time()
            print(f"Buffered write completed in {end_time - start_time:.4f} seconds.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up the file
        if os.path.exists("buffered_output.txt"):
            os.remove("buffered_output.txt")

buffered_write()