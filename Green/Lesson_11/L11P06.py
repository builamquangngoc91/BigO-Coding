class Student:
    def __init__(self, code, mark):
        self.code = code
        self.mark = mark


n, k = map(int, input().split())
array = []

for i in range(n):
    arr = input().split()
    array.append(Student(int(arr[0]), float(arr[1])))

for i in range(n - 1):
    for j in range(i + 1, n):
        if array[i].mark < array[j].mark or (array[i].mark == array[j].mark and array[i].code > array[j].code):
            array[i], array[j] = array[j], array[i]


for i in range(k):
    print(array[i].code)
