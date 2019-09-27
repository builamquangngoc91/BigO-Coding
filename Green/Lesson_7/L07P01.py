text = input().lower()

check_str = "bigo"

for char in text:
    if check_str.__contains__(char):
        print("YES")
        exit(0)

print("NO")
