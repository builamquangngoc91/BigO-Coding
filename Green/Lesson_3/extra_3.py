number = int(input())

arr = [4, 7]

for x in range(8, number + 1):
    check = False
    for el in arr:
        if x % el == 0:
            check = True
            break

    if check is False:
        check = True
        temp = x
        while temp > 0:
            if temp % 10 != 4 and temp % 10 != 7:
                check = False
                break
            temp //= 10

    if check:
        arr.append(x)

if arr.__contains__(number):
    print("YES")
else:
    print("NO")
