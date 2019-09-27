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

    def create_new_linked_list(self):
        new_linked_list = LinkedList()
        previous = 0
        temp = self.head
        while temp is not None:
            new_linked_list.insert_tail(Node(previous + temp.data))
            previous = temp.data
            temp = temp.next

        return new_linked_list

    def __str__(self):
        result = ""
        temp = self.head
        while temp is not None:
            result += str(temp.data) + " "
            temp = temp.next

        return result


linked_list = LinkedList()
n = int(input())
arr = list(map(int, input().split()))
for i in range(len(arr)):
    linked_list.insert_tail(Node(arr[i]))

print(linked_list.create_new_linked_list())

