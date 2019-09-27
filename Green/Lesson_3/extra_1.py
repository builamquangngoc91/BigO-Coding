number_of_stops = int(input())

max_number_of_passengers = 0
number_of_passengers = 0
for i in range(number_of_stops):
    a, b = map(int, input().split())
    number_of_passengers -= a
    number_of_passengers += b

    if number_of_passengers > max_number_of_passengers:
        max_number_of_passengers = number_of_passengers

print(max_number_of_passengers)
