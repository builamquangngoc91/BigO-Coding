n = int(input())

arr = list(map(int, input().split()))

max = 0

for i in range(n):
    if arr[i] > max:
        max = arr[i]

print(max)