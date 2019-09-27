class Vertex:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


n = int(input())
degrees = []

for i in range(n):
    args = list(map(int, input().split()))
    degrees.append(Vertex(args[0], args[1], args[2]))

min_w = 1001
count_d = 0

for i in range(n):
    if degrees[i].w < min_w:
        min_w = degrees[i].w
        count_d = 1
    elif degrees[i].w == min_w:
        count_d += 1

print(min_w * count_d)
