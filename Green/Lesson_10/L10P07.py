class Staff:
    def __init__(self, code, name, year_of_birth):
        self.code = code
        self.name = name
        self.year_of_birth = year_of_birth

    def __str__(self):
        return "{0} {1} {2}". format(self.code, self.name, self.year_of_birth)


n = int(input())

max_age = 0
min_code = 1000000
staff_result = None

for i in range(n):
    args = input().split()
    staff = Staff(args[0], args[1], int(args[2]))
    if max_age < 2019 - int(args[2]):
        staff_result = staff
        max_age = 2019 - int(args[2])
        min_code = int(args[0])
    elif max_age == 2019 - int(args[2]) and min_code > int(args[0]):
        min_code = int(args[0])
        staff_result = staff


print(staff_result)
