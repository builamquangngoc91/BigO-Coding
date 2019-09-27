n = int(input())
arr = list(map(int, input().split()))

index = -1

for i in range(1, 10000 + 1):
    check = True
    for j in range(n):
        if i == arr[j]:
            check = False
            break
    if check:
        index = i
        break

print(index)
