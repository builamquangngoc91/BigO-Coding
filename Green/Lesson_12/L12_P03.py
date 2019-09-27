import math


def is_prime_number(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False

    return True


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

    def calc_number_of_prime_numbers(self):
        count = 0
        temp = self.head
        while temp is not None:
            if is_prime_number(temp.data):
                count += 1

            temp = temp.next

        return count


linked_List = LinkedList()
while True:

    num = int(input())
    if num == -1:
        break
    linked_List.insert_tail(Node(num))

print(linked_List.calc_number_of_prime_numbers())
