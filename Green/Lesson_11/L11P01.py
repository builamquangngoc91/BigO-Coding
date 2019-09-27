num_of_elems = int(input())

arr = list(map(int, input().split()))

for i in range(num_of_elems - 1):
    for j in range(i + 1, num_of_elems):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

for i in range(num_of_elems):
    print(arr[i], end=" ")
