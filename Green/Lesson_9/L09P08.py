import sys
sys.setrecursionlimit(100)

n = int(input())


def recursion(i):
    if i == 0 or i == 1:
        return 1

    return recursion(i - 1) + recursion(i - 2)


print(recursion(n))
