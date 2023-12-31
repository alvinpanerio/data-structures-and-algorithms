# LL: Constructor


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        first_node = Node(value)
        self.head = first_node
        self.tail = first_node
        self.length = 1


my_linked_list = LinkedList(4)

print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print("Length:", my_linked_list.length)
