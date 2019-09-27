n = int(input())
arr = list(map(int, input().split()))

def is_prime_number(number_param):
    if number_param < 2:
        return False

    for i in range(2, number_param):
        if number_param % i == 0:
            return False

    return True

count_prime_numbers = 0

for i in range(n):
    if is_prime_number(arr[i]):
        count_prime_numbers += 1

print(count_prime_numbers)