import sys
sys.setrecursionlimit(20000)

n = int(input())
arr = list(map(int, input().split()))

def is_prime_number(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def recursion(i, arr_param):
    if i == n:
        return -1

    if is_prime_number(arr_param[i]):
        return i
    else:
        return recursion(i + 1, arr_param)


print(recursion(0, arr))
