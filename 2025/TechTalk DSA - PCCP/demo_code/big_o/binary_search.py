sorted_array = list(range(10, 20000001))

# caculate time the code runs
import time
start_time = time.time()

def binary_search(arr, target):
    
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Generate sorted array from 10 to 20 and do binary search 
target_value = 2000000
result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}")
else:
    print(f"Element {target_value} not found in the array")

end_time = time.time()
print(f"Time taken: {(end_time - start_time):.5f} seconds")