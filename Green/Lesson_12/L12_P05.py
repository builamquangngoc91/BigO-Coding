
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

    def remove_nodes_not_end_with_file(self):
        pre_node = None
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data % 10 == 5:
                if pre_node is None:
                    self.remove_head()
                    cur_node = self.head
                else:
                    self.remove_after(pre_node)
                    cur_node = pre_node.next
            else:
                pre_node = cur_node
                cur_node = cur_node.next
        return self

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
    num = int(input())
    linked_List.insert_tail(Node(num))

print(linked_List.remove_nodes_not_end_with_file())