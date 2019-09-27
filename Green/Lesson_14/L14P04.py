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

    def cal(self, sum_leaf):
        if self.left is not None:
            sum_leaf += self.left.cal(0)

        if self.right is not None:
            sum_leaf += self.right.cal(0)

        if self.left is None and self.right is None:
            sum_leaf += self.val

        return sum_leaf


class BST:
    def __init__(self):
        self.root = Node(-1)

    def add_to_BST(self, val):
        self.root = self.root.add_to_node(val)

    def cal_height(self):
        root = self.root.right
        return root.cal(0)


bst = BST()
n = int(input())
for number in list(map(int, input().split())):
    bst.add_to_BST(number)

print(bst.cal_height())
