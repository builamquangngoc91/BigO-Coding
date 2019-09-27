n = int(input())
arr = list(map(int, input().split()))

min_height = 1000

for i in range(n):
    if arr[i] < min_height:
        min_height = arr[i]

sum_height_reducing = 0

for i in range(n):
    sum_height_reducing += arr[i] - min_height

print(sum_height_reducing)