text = input()

for i in range(len(text)):
    if text[i] == "." and i + 2 < len(text) and text[i + 1] == " ":
        text = text[:i + 2] + text[i + 2].upper() + text[i + 3:]

print(text)
