number = int(input())


def is_symmetry_number(number_param):
    arr_elements = []

    while number_param > 0:
        arr_elements.append(number_param % 10)
        number_param //= 10

    for index in range(len(arr_elements) // 2):
        if arr_elements[index] != arr_elements[len(arr_elements) - index - 1]:
            return False

    return True


if is_symmetry_number(number):
    print("YES")
else:
    print("NO")
