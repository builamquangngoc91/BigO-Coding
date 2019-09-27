num_kms = int(input())

total_amount = 0

if 1 <= num_kms:
    total_amount += 15000

if 2 <= num_kms:
    temp = num_kms - 2 + 1
    if 5 < num_kms:
        temp = 4
    total_amount += 13500 * temp

if 6 <= num_kms:
    temp = num_kms - 6 + 1
    total_amount += 11000 * temp

if 12 <= num_kms:
    total_amount = int(total_amount * 0.9)

print(total_amount)