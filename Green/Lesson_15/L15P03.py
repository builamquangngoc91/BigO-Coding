n, x = map(int, input().split())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

degree = 0

for i in range(n):
    if matrix[x][i] == 1:
        degree += 1

print(degree)
