number = int(input())


def find_max_element_of_number(number_param):
    max = 0
    while number_param > 0:
        if max < number_param % 10:
            max = number_param % 10

        number_param //= 10
    return max


print(find_max_element_of_number(number))