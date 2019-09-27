count_stars = 0

while True:
    val = int(input())

    if val == 0:
        break

    if val == 5:
        count_stars += 1

print(count_stars)