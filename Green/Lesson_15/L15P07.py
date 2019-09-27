class Vertex:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


n, x = map(int, input().split())
degrees = []

for i in range(n):
    args = list(map(int, input().split()))
    degrees.append(Vertex(args[0], args[1], args[2]))


for i in range(n):
    for j in range(i + 1, n):
        if degrees[i].w > degrees[j].w:
            degrees[i], degrees[j] = degrees[j], degrees[i]

for i in range(x - 1, -1, -1):
    print("{0} {1}".format(degrees[i].u, degrees[i].v))
