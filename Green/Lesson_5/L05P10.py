n = int(input())
arr = list(map(int, input().split()))

number_of_zeros = 0

for i in range(n - 3):
    if arr[i] == 0 and arr[i + 1] == 0 and arr[i + 2] == 0 and arr[i + 3] == 0:
        print("NO")
        exit(0)

if arr[n - 1] == 0:
    print("NO")
else:
    print("YES")
