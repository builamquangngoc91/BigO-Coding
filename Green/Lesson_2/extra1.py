n, m, a = map(int, input().split())

w = n // a
h = m // a

if n % a != 0:
    w += 1

if m % a != 0:
    h += 1

print(w * h)