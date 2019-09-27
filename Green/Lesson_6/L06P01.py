num_of_rows, num_of_cols = map(int, input().split())

arr = []

for i in range(num_of_rows):
    row_arr = list(map(int, input().split()))
    arr.append(row_arr)

for i in range(num_of_rows):
    sum_of_rows = 0
    for j in range(num_of_cols):
        sum_of_rows += arr[i][j]
    print("{0}: {1}".format(i, sum_of_rows))
