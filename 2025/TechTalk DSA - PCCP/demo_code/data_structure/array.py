# Generate an array size 10, then create 3 functions to insert, update, delete in an element in it
class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            raise Exception("Array is full")
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def update(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.data[index] = value

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1
        self.data[self.size] = None

    def __str__(self):
        return str(self.data[:self.size])

# Example usage
arr = Array(10)
arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)
arr.insert(1, 15)
print(arr)
arr.update(0, 5)
print(arr)
arr.delete(1)
print(arr)
