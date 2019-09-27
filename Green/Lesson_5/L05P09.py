n = int(input())

max_orange, max_apple = 0, 0
index = 0

for i in range(n):
    apple, orange = map(int, input().split())
    if apple > max_apple:
        max_apple = apple
        max_orange = orange
        index = i
    elif apple == max_apple and orange > max_orange:
        max_orange = orange
        index = i

print(index + 1)
