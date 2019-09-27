steps = int(input())

result = steps // 5

if steps % 5 != 0:
    result += 1

print(result)