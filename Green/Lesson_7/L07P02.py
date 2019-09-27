text = input()

count_numbers = 0

for char in text:
    if "0" <= char <= "9":
        count_numbers += 1

print(count_numbers)
