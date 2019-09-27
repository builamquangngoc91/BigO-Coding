class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        if self.tail is None:
            self.tail = node

    def insert_tail(self, node):
        if self.head is None:
            self.head = node

        if self.tail is None:
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def print_marks_less_than_five(self):
        temp = self.head
        while temp is not None:
            if float(temp.data) < 5:
                print(temp.data)

            temp = temp.next


linked_List = LinkedList()
while True:

    num = input()
    if num == '-1':
        break
    linked_List.insert_tail(Node(num))

linked_List.print_marks_less_than_five()
