num_of_rows, num_of_cols = map(int, input().split())

arr = []

for i in range(num_of_rows):
    row_arr = list(map(int, input().split()))
    arr.append(row_arr)


def is_prime_number(number_param):
    if number_param < 2:
        return False

    for i in range(2, number_param):
        if number_param % i == 0:
            return False

    return True


count_prime_numbers = 0

for i in range(2, num_of_rows - 1):
    if is_prime_number(arr[i][0]):
        count_prime_numbers += 1
    if is_prime_number(arr[i][num_of_cols - 1]):
        count_prime_numbers += 1

for i in range(num_of_cols):
    if is_prime_number(arr[0][i]):
        count_prime_numbers += 1
    if is_prime_number(arr[num_of_rows - 1][i]):
        count_prime_numbers += 1

print(count_prime_numbers)
