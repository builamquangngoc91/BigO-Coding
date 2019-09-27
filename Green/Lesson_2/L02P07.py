begin, end = map(int, input().split())

num_of_electricity = end - begin

fee = 0

if num_of_electricity <= 50:
    fee += num_of_electricity * 1484
elif num_of_electricity > 50:
    fee += 50 * 1484

if 51 <= num_of_electricity <= 100:
    fee += (num_of_electricity - 50) * 1533
elif num_of_electricity > 100:
    fee += 50 * 1533

if 101 <= num_of_electricity <= 200:
    fee += (num_of_electricity - 100) * 1786
elif num_of_electricity > 200:
    fee += 100 * 1786

if 201 <= num_of_electricity <= 300:
    fee += (num_of_electricity - 200) * 2242
elif num_of_electricity > 300:
    fee += 100 * 2242

if 301 <= num_of_electricity <= 400:
    fee += (num_of_electricity - 300) * 2503
elif num_of_electricity > 400:
    fee += 100 * 2503

if num_of_electricity >= 401:
    fee += (num_of_electricity - 400) * 2587

print(fee + fee // 10)
