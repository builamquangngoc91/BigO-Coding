arr = []

for i in range(9):
    arr.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        temp = set()
        temp_1 = set()
        for z in range(9):
            temp.add(arr[i][z])
            temp_1.add(arr[z][j])

        if len(temp) != 9 or len(temp_1) != 9:
            print("NO")
            exit(0)

for i in range(3):
    for j in range(3):
        temp = set()
        for z in range(3):
            for k in range(3):
                temp.add(arr[3 * i + z][3 * j + k])

        if len(temp) != 9:
            print("NO")
            exit(0)

print("YES")


