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

    def remove_after(self, node):
        node_need_delete = node.next
        if node_need_delete is not None:
            if node_need_delete.next is not None:
                node.next = node_need_delete.next
                if node_need_delete.next is None:
                    self.tail = node_need_delete
            else:
                node.next = None
                self.tail = node

    def remove_head(self):
        if self.head is not None:
            self.head = self.head.next

    def find_second_max_number(self):
        max = -1
        second_max = -1
        temp = self.head
        while temp is not None:
            if temp.data > max:
                second_max = max
                max = temp.data
            if max > temp.data > second_max:
                second_max = temp.data
            temp = temp.next
        return second_max

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
while True:
    num = float(input())
    if num == -1:
        break
    linked_List.insert_tail(Node(num))

print(linked_List.find_second_max_number())
