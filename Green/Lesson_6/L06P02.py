num_of_rows, num_of_cols = map(int, input().split())

arr = []

for i in range(num_of_rows):
    row_arr = list(map(int, input().split()))
    arr.append(row_arr)

for i in range(num_of_cols):
    for j in range(num_of_rows):
        if arr[j][i] > 0:
            break
        elif arr[j][i] < 0 and j == num_of_rows - 1:
            print(i, end=' ')
