class Room:
    def __init__(self, code, price, status):
        self.code = code
        self.price = price
        self.status = status

    def __str__(self):
        return "{0} {1}".format(self.code, self.price)


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

    def print_rooms(self, status):
        temp = self.head
        while temp is not None:
            if temp.data.status == status:
                print(temp.data)

            temp = temp.next

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
n = int(input())
for i in range(n):
    temp = input().split()
    code = temp[0]
    price = int(temp[1])
    status = int(temp[2])
    linked_List.insert_tail(Node(Room(code, price, status)))

linked_List.print_rooms(0)
