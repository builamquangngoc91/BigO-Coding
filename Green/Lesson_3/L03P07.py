length = int(input())

for i in range(length):
    for j in range(length):
        if i == 0 or i == length - 1:
            print("*", end="")
            continue

        if j == 0 or j == length - 1:
            print("*", end="")
            continue

        print(" ", end="")
    print("\n", end="")
