number_of_cubes = int(input())

height = 0
sum_of_cubes = 0
sum_of_heights = 0

while sum_of_cubes < number_of_cubes:
    height += 1
    sum_of_heights += height
    sum_of_cubes += sum_of_heights

if sum_of_cubes == number_of_cubes:
    print(height)
else:
    print(height - 1)
