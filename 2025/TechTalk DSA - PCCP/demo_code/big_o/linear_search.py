sorted_array = list(range(10, 20000001))
# caculate time the code runs
import time
start_time = time.time()

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# Generate sorted array from 10 to 20 and do linear search 
target_value = 2000000
result = linear_search(sorted_array, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}")
else:
    print(f"Element {target_value} not found in the array")

end_time = time.time()
print(f"Time taken: {(end_time - start_time):.5f} seconds")