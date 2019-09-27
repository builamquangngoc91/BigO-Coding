text = input()

dictionary = {}

for i in range(len(text)):
    if dictionary.get(text[i]) is None:
        dictionary[text[i]] = True
    else:
        print(text[i])
        exit(0)

print("null")
