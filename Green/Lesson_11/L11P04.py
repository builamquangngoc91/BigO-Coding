num_elems = int(input())
array = list(map(int, input().split()))

for i in range(num_elems - 1):
    for j in range(i + 1, num_elems):
        if array[i] > array[j]:
            array[i] = array[i] + array[j]
            array[j] = array[i] - array[j]
            array[i] = array[i] - array[j]

if num_elems % 2 == 0:
    print("{0:.1f}".format((array[num_elems // 2 - 1] + array[num_elems // 2]) / 2))
else:
    print(array[num_elems // 2])
