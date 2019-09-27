text = input().lower()

arr = text.split(" ")

result = ""

for text_elem in arr:
    result += text_elem[0]

print(result)
