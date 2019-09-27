import math


class Point:
    def __init__(self, x_param, y_param):
        self.x = x_param
        self.y = y_param

    def distance(self, another_point):
        return math.sqrt(pow((self.x - another_point.x), 2) + pow((self.y - another_point.y), 2))

    def __str__(self):
        return "{0} {1}".format(self.x, self.y)


x_m, y_m = map(int, input().split())

point_m = Point(x_m, y_m)

n = int(input())

max_distance = 0
point_result = None

for i in range(n):
    x, y = map(int, input().split())
    point_temp = Point(x, y)

    if max_distance < point_temp.distance(point_m):
        max_distance = point_temp.distance(point_m)
        point_result = point_temp

print(point_result)
