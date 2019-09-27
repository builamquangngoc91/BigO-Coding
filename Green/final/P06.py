text = input()
a = ""
b = ""

for i in range(len(text)):
    if i % 2 == 0:
        a += text[i]
    else:
        b += text[i]

b = ''.join(reversed(b))



result = ""

a_i = 0
b_i = 0
for i in range(len(text)):
    if i % 2 == 0:
        result += a[a_i]
        a_i += 1
    else:
        result += b[b_i]
        b_i += 1

print(result)
