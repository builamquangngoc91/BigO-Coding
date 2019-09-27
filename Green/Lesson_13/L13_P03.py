n, x = map(int, input().split())
arr = list(map(int, input().split()))

check = False
for i in range(n):
    if arr[i] == x:
        print(i + 1, end=" ")
        check = True

if check is False:
    print(-1)
