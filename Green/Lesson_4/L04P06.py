number = int(input())


def is_prime_number(number_param):
    if number_param < 2:
        return False

    for num in range(2, number_param):
        if number_param % num == 0:
            return False

    return True


if is_prime_number(number):
    print(number)
    exit(0)


prime_number_less = 0
prime_number_rather = 0

temp = number - 1
while temp >= 2:
    if is_prime_number(temp):
        prime_number_less = temp
        break
    else:
        temp -= 1

temp = number + 1
while True:
    if is_prime_number(temp):
        prime_number_rather = temp
        break
    else:
        temp += 1

if prime_number_less == 0:
    print(prime_number_rather)
    exit(0)

if number - prime_number_less <= prime_number_rather - number:
    print(prime_number_less)
else:
    print(prime_number_rather)
