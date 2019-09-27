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

    def min(self):
        result_min = 100001
        temp = self.head
        while temp is not None:
            if temp.data < result_min:
                result_min = temp.data

            temp = temp.next

        return result_min


linked_List = LinkedList()
while True:
    num = int(input())
    if num == 0:
        break
    linked_List.insert_tail(Node(num))

print(linked_List.min())
