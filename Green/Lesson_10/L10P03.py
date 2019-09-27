class Student:
    def __init__(self, name, math_mark, literature_mark):
        self.name = name
        self.math_mark = math_mark
        self.literature_mark = literature_mark

    def calculate_mark_average(self):
        return (self.math_mark + self.literature_mark) / 2


num_students = int(input())

count_students_rather_than_9 = 0


for i in range(num_students):
    name = input()
    math_mark, literature_mark = map(float, input().split())
    student = Student(name, math_mark, literature_mark)
    if student.calculate_mark_average() >= 9:
        count_students_rather_than_9 += 1


print(count_students_rather_than_9)
