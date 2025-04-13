class ProbingHashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity


    def _hash(self, key):
        # Custom hash function to increase collision likelihood
        if isinstance(key, str):
            return sum(ord(char) for char in key) % self.capacity
        elif isinstance(key, int):
            return key % self.capacity
        else:
            raise TypeError("Unsupported key type")


    def put(self, key, value):
        index = self._hash(key)
        for _ in range(self.capacity):
            if self.table[index] is None or self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.capacity
        raise Exception("HashMap is full")

    def get(self, key):
        index = self._hash(key)
        for _ in range(self.capacity):
            if self.table[index] is None:
                return None
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity
        return None

    def remove(self, key):
        index = self._hash(key)
        for _ in range(self.capacity):
            if self.table[index] is None:
                return
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.capacity


class ChainingHashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]


    def _hash(self, key):
        # Custom hash function to increase collision likelihood
        if isinstance(key, str):
            return sum(ord(char) for char in key) % self.capacity
        elif isinstance(key, int):
            return key % self.capacity
        else:
            raise TypeError("Unsupported key type")


    def put(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return


# Example usage:
if __name__ == "__main__":
    print("Probing HashMap:")
    probing_map = ProbingHashMap()
    probing_map.put("a", 1)
    probing_map.put("b", 2)
    print(probing_map.get("a"))  # Output: 1
    probing_map.remove("a")
    print(probing_map.get("a"))  # Output: None

    print("\nChaining HashMap:")
    chaining_map = ChainingHashMap()
    chaining_map.put("a", 1)
    chaining_map.put("b", 2)
    print(chaining_map.get("a"))  # Output: 1
    chaining_map.remove("a")
    print(chaining_map.get("a"))  # Output: None