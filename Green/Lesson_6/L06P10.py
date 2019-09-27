num_of_rows, num_of_cols = map(int, input().split())

a, b, p = map(int, input().split())

for i in range(num_of_rows):
    for j in range(num_of_cols):
        space = " "

        if j == num_of_cols - 1:
            space = ""

        if i == 0:
            if j == 0:
                print(a, end=space)
                continue
            if j == 1:
                print(b, end=space)
                continue

        c = (a + b) % p
        a = b
        b = c
        print(c, end=space)

    if i != num_of_rows - 1:
        print("\n", end="")
