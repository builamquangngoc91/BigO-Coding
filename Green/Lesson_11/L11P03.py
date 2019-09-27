import math

num_elems = int(input())
array = list(map(int, input().split()))


def is_prime_number(number):
    if number < 2:
        return False

    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


for i in range(num_elems - 1):
    for j in range(i + 1, num_elems):
        if is_prime_number(array[i]) is False and is_prime_number(array[j]) is False and array[i] > array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

print(*array, end=" ")
