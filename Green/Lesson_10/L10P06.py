class Color:
    def __init__(self, code, length):
        self.code = code
        self.length = length


class ColorAppearLength:
    def __init__(self, code, appear, length):
        self.code = code
        self.appear = appear
        self.length = length

    def __str__(self):
        return "{0} {1} {2}".format(self.code, self.length, self.appear)


num_colors = int(input())

dict_color_appear_length = {}

for i in range(num_colors):
    code, length = map(int, input().split())
    if dict_color_appear_length.get(code) is None:
        dict_color_appear_length[code] = ColorAppearLength(code, 1, length)
    else:
        dict_color_appear_length[code].appear += 1
        dict_color_appear_length[code].length += length

print(len(dict_color_appear_length))

for el in sorted(dict_color_appear_length.items()):
    print(dict_color_appear_length[el[0]])
