num_elems = int(input())
array = list(map(int, input().split()))

for i in range(num_elems - 1):
    for j in range(i + 1, num_elems):
        if array[i] % 2 == 0 and array[j] % 2 == 0 and array[i] > array[j]:
            array[i], array[j] = array[j], array[i]
        if array[i] % 2 != 0 and array[j] % 2 != 0 and array[i] < array[j]:
            array[i], array[j] = array[j], array[i]

print(*array, end=" ")
