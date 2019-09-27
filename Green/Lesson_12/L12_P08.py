class date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # -1 less
    # 0 equal
    # 1 greater
    def compare(self, another_date):
        if self.year > another_date.year:
            return 1
        if self.year < another_date.year:
            return -1

        if self.month > another_date.month:
            return 1
        if self.month < another_date.month:
            return -1

        if self.day > another_date.day:
            return 1
        if self.day == another_date.day:
            return 0
        if self.day < another_date.day:
            return -1

    def __str__(self):
        return "{0} {1} {2}".format(self.day, self.month, self.year)


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

    def find_newest_date(self):
        newest_date = date(0, 0, 0)
        temp = self.head
        while temp is not None:
            if temp.data.compare(newest_date) == 1:
                newest_date = temp.data

            temp = temp.next
        return newest_date

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
    d, m, y = map(int, input().split())
    linked_List.insert_tail(Node(date(d, m, y)))

print(linked_List.find_newest_date())
