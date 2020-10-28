# import pygame


class A:
    name = "A"

    def __init__(self, a):
        print("A.__init__")
        self.a = a

    def aa(self):
        print("A method")


def func():
    obj = A(5)
    obj.aa()
    return obj


Z = A


class B(Z):
    name = "B"

    def __init__(self, *a, **kw):
        print("B.__init__")
        super().__init__(*a, **kw)


A = B

print(func().__dict__)
print(type(func()).__dict__)