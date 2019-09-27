number_of_lines = int(input())

array = ""

for i in range(number_of_lines):
    text = " " + input()

    for j in range(len(text) - 1):
        if text[j] == " ":
            text = text[:j + 1] + text[j + 1].upper() + text[j + 2:]
        else:
            if text[j + 1] != " ":
                text = text[:j + 1] + text[j + 1].lower() + text[j + 2:]

    print(text[1:])
