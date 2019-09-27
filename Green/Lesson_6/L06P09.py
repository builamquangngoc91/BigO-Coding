num_of_rows, num_of_cols = map(int, input().split())

arr = []

for i in range(num_of_rows):
    row_arr = list(map(int, input().split()))
    arr.append(row_arr)

count_saddle_numbers = 0

for i in range(num_of_rows):
    for j in range(num_of_cols):
        max_number = 0
        min_number = 1000
        for z in range(num_of_rows):
            if arr[z][j] < min_number:
                min_number = arr[z][j]

        for z in range(num_of_cols):
            if arr[i][z] > max_number:
                max_number = arr[i][z]

        if arr[i][j] == max_number and arr[i][j] == min_number:
            count_saddle_numbers += 1

print(count_saddle_numbers)
