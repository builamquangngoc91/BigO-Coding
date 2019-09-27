s = input()
number_of_steps = int(input())

for index in range(number_of_steps):
    step = input()
    start = int(step.split(" ")[1])
    length = int(step.split(" ")[2])
    if step[0] == "d":
        s = s[:start - 1] + s[start + length - 1:]
    elif step[0] == "c":
        print(s[start - 1:start + length - 1])
