import sys
sys.setrecursionlimit(1000000)

a, b = map(int, input().split())


def recursion(a, b):
    if b == 0:
        return a
    else:
        return recursion(b, a % b)


print(recursion(a, b))
