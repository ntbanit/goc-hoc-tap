import os
import time

def non_buffered_write():
    # 'wb' is write binary mode. buffering=0 forces OS-level I/O on every single write.
    # This is typically only done for low-level or specialized tasks.
    try:
        with open("unbuffered_output.bin", "wb", buffering=0) as f:
            start_time = time.time()
            for i in range(100000):
                # Each f.write() call hits the OS boundary immediately.
                f.write(b"data")
            end_time = time.time()
            print(f"Non-buffered write completed in {end_time - start_time:.4f} seconds.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("# Clean up the file")
        if os.path.exists("unbuffered_output.bin"):
           os.remove("unbuffered_output.bin")

non_buffered_write()