text = " " + input()

text_result = ""

flag = True

while text.__contains__(" ") is True:
    text_result = text_result + text[text.rfind(" ") + 1:] + " "
    text = text[: text.rfind(" ")]

print(text_result[: len(text_result) - 1])
