import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def add_to_node(self, val):
        new_node = Node(val)

        root = self
        while root is not None:
            if val < root.val:
                if root.left is None:
                    root.left = new_node
                    return self

                root = root.left
            elif root.val < val:
                if root.right is None:
                    root.right = new_node
                    return self

                root = root.right
            else:
                return self
        return self

    def cal(self):
        if self.left is not None:
            self.left.cal()

        if self.right is not None:
            self.right.cal()

        if self.val % 2 == 0:
            print(self.val, end=" ")


class BST:
    def __init__(self):
        self.root = Node(-1)

    def add_to_BST(self, val):
        self.root = self.root.add_to_node(val)

    def cal_height(self):
        root = self.root.right
        return root.cal()


bst = BST()
n = int(input())
for number in list(map(int, input().split())):
    bst.add_to_BST(number)

bst.cal_height()
