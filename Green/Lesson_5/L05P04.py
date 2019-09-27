n = int(input())
arr = list(map(int, input().split()))

check = True

for i in range(n):
    if arr[i] == 0:
        check = False
        break

if check:
    print("YES")
else:
    print("NO")
