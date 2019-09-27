number = int(input())

sum_of_ele = 0

while number / 10 > 0:
    sum_of_ele += number % 10
    number //= 10

print(sum_of_ele % 10)



