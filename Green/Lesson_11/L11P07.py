def partition(arr, start, end):
    i = (start - 1)
    pivot = arr[end]

    for j in range(start, end):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        index = partition(arr, start, end)
        quick_sort(arr, start, index - 1)
        quick_sort(arr, index + 1, end)


array = [10, 7, 8, 9, 1, 5]
n = len(array)
quick_sort(array, 0, len(array) - 1)
print(*array, end=" ")
