import math


class Point:
    def __init__(self, x_param, y_param):
        self.x = x_param
        self.y = y_param

    def distance(self, another_point):
        return math.sqrt(pow((self.x - another_point.x), 2) + pow((self.y - another_point.y), 2))

    def __str__(self):
        return "{0} {1}".format(self.x, self.y)


class Rectangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        a = self.x.distance(self.y)
        b = self.y.distance(self.z)
        c = self.z.distance(self.x)
        p = (a + b + c) / 2
        return math.sqrt(p*(p - a)*(p - b)*(p - c))


num_rectangles = int(input())

sum = 0

for i in range(num_rectangles):
    points = []
    for j in range(3):
        x, y = map(int, input().split())
        points.append(Point(x, y))

    rectangle = Rectangle(points[0], points[1], points[2])
    sum += rectangle.area()

print("{0:.2f}".format(sum))
