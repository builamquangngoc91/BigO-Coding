n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

adjacency_list = []
count = 0

for i in range(n):
    adjacency_list.append([])
    for j in range(n):
        if matrix[i][j] == 1:
            adjacency_list[i].append(j)
            count += 1

print(count)
for i in range(len(adjacency_list)):
    for j in range(len(adjacency_list[i])):
        print("{0} {1}".format(i, adjacency_list[i][j]))
