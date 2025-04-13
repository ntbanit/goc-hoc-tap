# Queue implementation using an array
class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        raise IndexError("Dequeue from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        raise IndexError("Peek from an empty queue")

    def size(self):
        return len(self.queue)


# Queue implementation using a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node
        self._size += 1

    def dequeue(self):
        if not self.is_empty():
            value = self.front.value
            self.front = self.front.next
            if not self.front:
                self.rear = None
            self._size -= 1
            return value
        raise IndexError("Dequeue from an empty queue")

    def is_empty(self):
        return self.front is None

    def peek(self):
        if not self.is_empty():
            return self.front.value
        raise IndexError("Peek from an empty queue")

    def size(self):
        return self._size


# Demonstration with 5 elements
if __name__ == "__main__":
    print("Using ArrayQueue:")
    array_queue = ArrayQueue()
    for i in range(1, 6):
        array_queue.enqueue(i)
    while not array_queue.is_empty():
        print(array_queue.dequeue(), end=" ")
    print("\n")

    print("Using LinkedListQueue:")
    linked_list_queue = LinkedListQueue()
    for i in range(1, 6):
        linked_list_queue.enqueue(i)
    while not linked_list_queue.is_empty():
        print(linked_list_queue.dequeue(), end=" ")
    print()