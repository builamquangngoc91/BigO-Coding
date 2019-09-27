n = int(input())

arr = []

for i in range(n):
    row_arr = list(map(int, input().split()))
    arr.append(row_arr)

count_queens = 0

for i in range(n):
    for j in range(n):
        max_number = 0
        for z in range(n):
            if arr[z][j] > max_number:
                max_number = arr[z][j]
        for z in range(n):
            if arr[i][z] > max_number:
                max_number = arr[i][z]

        z = 0
        while i - z > 0 and j - z > 0:
            if arr[i -z][j - z] > max_number:
                max_number = arr[i - z][j - z]
            z += 1

        z = 0
        while i + z < n and j + z < n:
            if arr[i + z][j + z] > max_number:
                max_number = arr[i + z][j + z]
            z += 1

        z = 0
        while i - z > 0 and j + z < n:
            if arr[i - z][j + z] > max_number:
                max_number = arr[i - z][j + z]
            z += 1

        z = 0
        while i + z < n and j - z > 0:
            if arr[i + z][j - z] > max_number:
                max_number = arr[i + z][j - z]
            z += 1

        if arr[i][j] == max_number:
            count_queens += 1

print(count_queens)
