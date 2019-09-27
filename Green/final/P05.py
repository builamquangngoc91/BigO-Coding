arr = []
for i in range(4):
    arr.append(list(map(int, input().split())))

for i in range(4):
    if arr[i][0] == 1:
        if arr[i - 1][3] == 1 or arr[i][3] == 1:
            print("YES")
            exit(0)

    if arr[i][1] == 1:
        if arr[(i + 2) % 4][3] == 1 or arr[i][3] == 1:
            print("YES")
            exit(0)

    if arr[i][2] == 1:
        if arr[(i + 1) % 4][3] == 1 or arr[i][3] == 1:
            print("YES")
            exit(0)

print("NO")
exit(0)

