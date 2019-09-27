n = abs(int(input()))


def recursion(max, number):
    if number == 0:
        if max > number:
            return max
        else:
            return number

    if max < number % 10:
        max = number % 10

    return recursion(max, number // 10)


print(recursion(0, n))
