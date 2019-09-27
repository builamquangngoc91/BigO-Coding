min = 11
max = -1

while True:
    val = int(input())

    if val == -1:
        break

    if val > max:
        max = val

    if val < min:
        min = val

print(max, min)