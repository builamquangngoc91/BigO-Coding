number_of_candy_box = int(input())

check = True

for x in range(number_of_candy_box):
    number_of_candies = int(input())

    if number_of_candies % 2 == 1:
        check = False
        break

if check:
    print("YES")
else:
    print("NO")