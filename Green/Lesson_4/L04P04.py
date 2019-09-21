number = int(input())


def count_elements_of_number(number_param):
    count = 0
    while number_param > 0:
        count += 1
        number_param //= 10

    return count


print(count_elements_of_number(number))