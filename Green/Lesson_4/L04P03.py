a, b = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


gcd_a_b = gcd(a, b)

print(int(a / gcd_a_b), int(b / gcd_a_b))
