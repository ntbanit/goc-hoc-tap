#Implement stack with array and linked list
class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        if not self.is_empty():
            value = self.head.value
            self.head = self.head.next
            self._size -= 1
            return value
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.head.value
        raise IndexError("Peek from empty stack")

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

# Example usage
# Using StackArray
stack_array = StackArray()
for i in range(1, 6):
    stack_array.push(i)

print("StackArray:")
while not stack_array.is_empty():
    print(stack_array.pop())

# Using StackLinkedList
stack_linked_list = StackLinkedList()
for i in range(1, 6):
    stack_linked_list.push(i)

print("\nStackLinkedList:")
while not stack_linked_list.is_empty():
    print(stack_linked_list.pop())