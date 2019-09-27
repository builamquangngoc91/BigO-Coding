import sys

sys.setrecursionlimit(10000)

n = int(input())


def divisor(number, i):
    if number % i == 0 and i % 2 == 1:
        return i
    return divisor(number, i // 2)


print(divisor(n, n))
