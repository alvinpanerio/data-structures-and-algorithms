# LL: Constructor


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        # return True

    # my solution
    def pop(self):
        if self.head is not None and self.tail is not None:
            temp = self.head
            while temp:
                if self.length == 1:
                    self.head = None
                    self.tail = None
                    self.length -= 1
                    return temp

                if temp.next is self.tail:
                    tempVal = temp.next
                    temp.next = None
                    self.tail = temp
                    self.length -= 1
                    return tempVal
                temp = temp.next
        else:
            return None


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.pop()

my_linked_list.print_list()
