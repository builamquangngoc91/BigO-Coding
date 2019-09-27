previous_length = 1

check = True


while True:
    val = int(input())

    if val == 0:
        break

    if previous_length > val:
        check = False
        break

    previous_length = val

if check:
    print("YES")
else:
    print("NO")

