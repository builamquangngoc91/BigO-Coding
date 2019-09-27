n = int(input())

if n % 2 == 1:
    print("NO")
    exit(0)

arr = list(map(int, input().split()))

number_of_boys = 0
number_of_girls = 0

for i in range(n):
    if arr[i] == 0:
        number_of_boys += 1
    else:
        number_of_girls += 1

if number_of_boys == number_of_girls:
    print("YES")
else:
    print("NO")
