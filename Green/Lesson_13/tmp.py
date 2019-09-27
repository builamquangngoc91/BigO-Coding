class A:
    def __init__(self, a):
        self.a = a


b = A(1)
c = b

if b is c:
    print("True")
else:
    print("False")
