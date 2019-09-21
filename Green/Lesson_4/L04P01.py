number = int(input())


def is_prime_number(number_param):
    if number_param < 2:
        return False

    for num in range(2, number_param):
        if number_param % num == 0:
            return False

    return True


sum_prime_numbers = 0

for num in range(2, number):
    if is_prime_number(num):
        sum_prime_numbers += num

print(sum_prime_numbers)
