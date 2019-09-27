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

    def __str__(self):
        result = ""
        temp = self.head
        while temp is not None:
            result += str(temp.data) + " "
            temp = temp.next

        return result


x, y, n = map(int, input().split())

linkedList = LinkedList()
first_temp = 0
second_temp = 0
for i in range(n):
    if i == 0:
        first_temp = x
        linkedList.insert_tail(Node(x))
        continue
    if i == 1:
        second_temp = y
        linkedList.insert_tail(Node(y))
        continue

    linkedList.insert_tail(Node((first_temp + second_temp) % 1000007))
    first_temp, second_temp = second_temp, (first_temp + second_temp) % 1000007

print(linkedList)
