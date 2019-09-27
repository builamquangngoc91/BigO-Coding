num_of_rows, num_of_cols = map(int, input().split())

arr = []

for i in range(num_of_rows):
    row_arr = list(map(int, input().split()))
    arr.append(row_arr)

max_even_numbers = 0
index_row = 0

for i in range(num_of_rows):
    count_even_numbers = 0
    for j in range(num_of_cols):
        if arr[i][j] % 2 == 0:
            count_even_numbers += 1
    if max_even_numbers < count_even_numbers:
        max_even_numbers = count_even_numbers
        index_row = i

print(index_row)
