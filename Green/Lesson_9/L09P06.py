import sys
sys.setrecursionlimit(20000)

n = int(input())
arr = list(map(int, input().split()))


def recursion(i, arr_param):
    if i == n:
        return 0

    if arr_param[i] % 2 == 0:
        return arr_param[i] + recursion(i + 1, arr_param)
    else:
        return recursion(i + 1, arr_param)


print(recursion(0, arr))
