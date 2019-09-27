class Block:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __str__(self):
        return "{0} {1}".format(self.x, self.y)


m, n = map(int, input().split())

arr = []
max_sum = 0

k = int(input())

for i in range(k):
    x, y, value = map(int, input().split())

    if value > 0:
        arr.append(Block(x, y, value))
        max_sum += value

print(len(arr))
for i in range(len(arr)):
    print(arr[i])
