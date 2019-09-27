n = int(input())

arr = []

for i in range(n):
    arr.append(input())

count = 0
temp = arr[0]
for i in range(1, n):
    if arr[i] != temp:
        count += 1
        temp = arr[i]

print(count + 1)
