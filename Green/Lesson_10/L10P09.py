class Fraction:
    def __init__(self, num_param, denom_param):
        self.num = num_param
        self.denom = denom_param

    def reduce_fraction(self):
        if self.num == 0:
            self.denom = 1
        else:
            x = self.gcd(abs(self.num), abs(self.denom))
            self.num = self.num // x
            self.denom = self.denom // x
        return self

    def gcd(self, a, b):
        r = 0
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    def value(self):
        return self.num / self.denom

    def __str__(self):
        return "{0} {1}".format(self.num, self.denom)


n = int(input())

max_fraction = 0
fraction_result = 0

for i in range(n):
    num, denom = map(int, input().split())
    fraction = Fraction(num, denom)
    if max_fraction <= fraction.value():
        max_fraction = fraction.value()
        fraction_result = fraction


print(fraction_result.reduce_fraction())
