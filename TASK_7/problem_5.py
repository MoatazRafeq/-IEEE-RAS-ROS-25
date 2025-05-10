class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

# Example usage
ll = LinkedList()

# Creating initial linked list
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)

print("Initial Linked List:")
ll.display()

# Inserting a new node
ll.insert(5)
print("After insert a new node (5):")
ll.display()

# Deleting an existing node
ll.delete(2)
print("After delete a existing node (2):")
ll.display()