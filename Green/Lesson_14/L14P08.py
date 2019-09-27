import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, code, name, val=0):
        self.name = name
        self.code = code
        self.val = val
        self.left = None
        self.right = None

    def add_to_node(self, name, code, val):
        new_node = Node(name, code, val)

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

    def cal(self, node_max):
        if self.left is not None:
            temp = self.left.cal(node_max)
            if temp.val > node_max.val:
                node_max = temp

        if self.right is not None:
            temp = self.right.cal(node_max)
            if temp.val > node_max.val:
                node_max = temp

        if node_max.val < self.val:
            node_max = self

        return node_max


class BST:
    def __init__(self):
        self.root = Node("", "", -1)

    def add_to_BST(self, code, name, val):
        self.root = self.root.add_to_node(code, name, val)

    def cal_height(self):
        root = self.root.right
        return root.cal(root)


bst = BST()
n = int(input())
for i in range(n):
    arr = input().split()
    bst.add_to_BST(arr[0], arr[1], float(arr[2]))

result = bst.cal_height()
print(result.code, result.name, result.val)
