num_of_rows, num_of_cols = map(int, input().split())

arr = []

for i in range(num_of_rows):
    row_arr = list(map(int, input().split()))
    arr.append(row_arr)

count_images_rather_than_100_likes = 0

for i in range(num_of_rows):
    for j in range(num_of_cols):
        if arr[i][j] > 100:
            count_images_rather_than_100_likes += 1

print(count_images_rather_than_100_likes)
