a, b = map(int, input().split())
c, d = map(int, input().split())

for i in range(0, 101):
    for j in range(0, 101):
        if b + i * a == d + j * c:
            print(b + i * a)
            exit(0)


print(-1)

