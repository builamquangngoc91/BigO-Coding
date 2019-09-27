n, k = map(int, input().split())

scores = list(map(int, input().split()))

count = 0

for i in range(k):
    if scores[i] > 0:
        count += 1

if scores[k - 1] > 0:
    for i in range(k, n):
        if scores[i] == scores[k - 1]:
            count += 1

print(count)
