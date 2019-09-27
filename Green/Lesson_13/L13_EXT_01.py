class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_tail(self, another_node):
        if self.head is None:
            self.head = another_node
            self.tail = another_node
        else:
            self.tail.next = another_node
            self.tail = another_node

    def reverse(self):
        previous = None
        head = None

        self.tail = self.head
        cur = self.head
        while cur is not None:
            head = cur.next
            cur.next = previous
            previous = cur
            cur = head

        self.head = previous

        return self

    def __str__(self):
        result = ""
        temp = self.head
        while temp is not None:
            result += str(temp.data) + "->"
            temp = temp.next

        return result


text = input()
arr = text[:len(text)-6].split("->")
linked_list = LinkedList()
for el in arr:
    linked_list.insert_tail(Node(el))

print(str(linked_list.reverse()) + "NULL")
