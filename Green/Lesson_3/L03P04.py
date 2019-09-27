prime_number = int(input())

count_divisors = 1

for x in range(2, prime_number + 1):
    if prime_number % x == 0:
        count_divisors += 1

    if count_divisors > 2:
        break

if count_divisors == 2:
    print("YES")
else:
    print("NO")
