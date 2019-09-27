n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            print("NO")
            exit(0)

print("YES")
