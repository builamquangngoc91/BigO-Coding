n = int(input())
arr = list(map(int, input().split()))

count_numbers_less_than_zero = 0
less_than_zero = []

count_numbers_rather_than_zero = 0
rather_than_zero = []

count_numbers_equal_zero = 0
equal_zero = []

for i in range(n):
    if arr[i] < 0:
        count_numbers_less_than_zero += 1
        less_than_zero.append(arr[i])
    elif arr[i] > 0:
        count_numbers_rather_than_zero += 1
        rather_than_zero.append(arr[i])
    else:
        count_numbers_equal_zero += 1
        equal_zero.append(arr[i])

print(count_numbers_less_than_zero, *less_than_zero)
print(count_numbers_rather_than_zero, *rather_than_zero)
print(count_numbers_equal_zero, *equal_zero)

