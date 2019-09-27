import sys

sys.setrecursionlimit(10000)

n = abs(int(input()))


def recursion(number):
    if number == 0:
        return 0
    return 1 + recursion(number // 10)


if n == 0:
    print(1)
else:
    print(recursion(n))
