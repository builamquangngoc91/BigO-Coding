class Student:
    def __init__(self, code, math_mark, literature_mark):
        self.code = code
        self.math_mark = math_mark
        self.literature_mark = literature_mark

    def __str__(self):
        return "{0} {1}".format(self.math_mark, self.literature_mark)


n, q = map(int, input().split())

students_dict = {}

for i in range(n):
    code, math_mark, literature_mark = map(float, input().split())
    students_dict[code] = Student(code, math_mark, literature_mark)

for i in range(q):
    code = int(input())
    print(students_dict[code])
