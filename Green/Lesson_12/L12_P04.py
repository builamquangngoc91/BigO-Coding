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

    def __str__(self):
        result = ""
        temp = self.head
        while temp is not None:
            result += str(temp.data)

            if temp.next is not None:
                result += " "

            temp = temp.next

        return result


linked_List = LinkedList()
index = 1
while True:
    num = int(input())
    if num == 0:
        break

    linked_List.insert_tail(Node(index))
    linked_List.insert_tail(Node(num))

    index += 1

print(linked_List)
