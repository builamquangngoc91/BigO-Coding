class Fraction:
    def __init__(self, num_param, denom_param):
        self.num = num_param
        self.denom = denom_param

    def reduce_fraction(self):
        if self.num == 0:
            self.denom = 1
            return
        x = self.gcd(abs(self.num), abs(self.denom))
        self.num = self.num // x
        self.denom = self.denom // x
        return self

    def sum_fraction(self, another_fraction):
        num = self.num * another_fraction.denom + another_fraction.num * self.denom
        denom = self.denom * another_fraction.denom
        return Fraction(num, denom).reduce_fraction()

    def gcd(self, a, b):
        r = 0
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    def __str__(self):
        return "{0} {1}".format(self.num, self.denom)


num, denom = map(int, input().split())
fac_1 = Fraction(num, denom)

num, denom = map(int, input().split())
fac_2 = Fraction(num, denom)

result = fac_1.sum_fraction(fac_2)

print(result)

