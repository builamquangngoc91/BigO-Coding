a = int(input())
b = int(input())
c = int(input())

max_result = a + b + c

if a * b + c > max_result:
    max_result = a * b + c
if a + b * c > max_result:
    max_result = a + b * c
if (a + b) * c > max_result:
    max_result = (a + b) * c
if a * (b + c) > max_result:
    max_result = a * (b + c)
if a * b * c > max_result:
    max_result = a * b * c

print(max_result)
