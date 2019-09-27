number_of_lines = int(input())

for i in range(number_of_lines):
    text = input().lower()

    dictionary = {}
    for char in text:
        if dictionary.__contains__(char):
            dictionary[char] = dictionary[char] + 1
        else:
            dictionary[char] = 1

    min = 1000
    min_key = ""
    for k, v in dictionary.items():
        if v < min:
            min = v
            min_key = k
        elif v == min and k < min_key:
            min_key = k

    print(min_key.upper())
