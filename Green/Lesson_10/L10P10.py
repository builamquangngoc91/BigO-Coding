highest_price = 0
highest_weight = 0
highest_index_apple = None

num_apples = int(input())

for i in range(num_apples):
    weight, price = map(int, input().split())

    if weight > highest_weight:
        highest_weight = weight
        highest_price = price
        highest_index_apple = i
    elif weight == highest_weight and price > highest_price:
        highest_index_apple = i
        highest_price = price

print(highest_index_apple)
