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

count_d = 0
mul_w = 1

for i in range(n):
    if degrees[i].u == degrees[i].v:
        mul_w = (mul_w * degrees[i].w) % 1000007
        count_d += 1

if count_d == 0:
    print(-1)
else:
    print(count_d, mul_w)
