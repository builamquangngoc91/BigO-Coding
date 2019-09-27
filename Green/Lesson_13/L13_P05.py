length = int(input())
text = input()


def recursion(i, n, text_param):
    if i >= n // 2:
        return True
    return text_param[i] == text_param[n - i - 1] and recursion(i + 1, n, text_param)


if recursion(0, length, text):
    print("YES")
else:
    print("NO")
