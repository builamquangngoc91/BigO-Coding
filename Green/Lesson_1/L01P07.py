a, b, c = map(float, input().split())

P = a + b + c
p = P / 2
S = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

print('{0:.2f} {1:.2f}'.format(P, S))