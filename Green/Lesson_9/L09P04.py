n = abs(int(input()))


def recursion(number):
    if number < 10:
        return number
    return recursion(number // 10)


print(recursion(n))
