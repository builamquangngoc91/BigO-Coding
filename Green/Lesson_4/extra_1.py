n, m = map(int, input().split())

min = n

if m < min:
    min = m

count = 0

for number in range(min + 1):
    a = number
    b = n - a ** 2

    if b < 0:
        continue

    if a + b ** 2 == m:
        count += 1

print(count)