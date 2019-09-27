upan, ipan = map(int, input().split())
x = int(input())

if x % upan == 0 and x % ipan == 0:
    print("Both")
elif x % upan == 0:
    print("Upan")
elif x % ipan == 0:
    print("Ipan")
else:
    print("No")
