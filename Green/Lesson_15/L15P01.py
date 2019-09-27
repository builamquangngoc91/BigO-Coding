n = int(input())
adjacency_matrix = []

for i in range(n):
    adjacency_matrix.append(list(map(int, input().split())))

num = 0
arr = []

for i in range(n):
    for j in range(i + 1, n):
        if adjacency_matrix[i][j] == 1:
            arr.append("{0} {1}".format(i, j))
            num += 1

print(num)

for i in range(num):
    print(arr[i])
