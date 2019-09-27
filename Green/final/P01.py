import sys

sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a + b


def merge(l, arr_l, r, arr_r, n, arr):
    i, j, k = 0, 0, 0
    while i < l and j < r:
        if arr_l[i] > arr_r[j]:
            arr[k] = arr_r[j]
            j += 1
        else:
            arr[k] = arr_l[i]
            i += 1
        k += 1

    for z in range(i, len(arr_l)):
        arr[k] = arr_l[z]
        k += 1

    for z in range(j, len(arr_r)):
        arr[k] = arr_r[z]
        k += 1

    return arr


def merge_sort(n, arr):
    if len(arr) < 2:
        return arr

    mid = n // 2
    l, r = mid, n - mid
    arr_l = arr[:mid]
    arr_r = arr[mid:]

    merge_sort(l, arr_l)
    merge_sort(r, arr_r)
    return merge(l, arr_l, r, arr_r, n, arr)


m = merge_sort(m + n, c)

print(m[k])
