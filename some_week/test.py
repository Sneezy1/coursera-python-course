class B:
    n = 5
    def adder(self, v):
        return v + self.n


l = B()
m = B()
l.n = 10
l.adder(3)
print(B.n)
print(l.n)
print(m.adder(4))
print(m.n)
B.adder(B, 2)
print(B.n)
print(l.__dict__)


class Rectangle:
    def __init__(self, w=0.5, h=1):
        self.width = w
        self.height = h

    def square(self):
        return self.width * self.height


rec1 = Rectangle(5, 2)
rec2 = Rectangle()
rec3 = Rectangle(3)
rec4 = Rectangle(h=4)
print(rec1.square())
print(rec2.square())
print(rec3.square())
print(rec4.square())

del rec1
print(rec1)



class ComputerTable(DeskTable):
    def square(self, e):
        return DeskTable.square(self) - e



class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        self.length = l
        self.width = w
        self.height = h
        self.places = p


class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        Table.__init__(self, l, w, h)
        self.places = p



class A:
    def __init__(self, v):
        self.field1 = v
    def __setattr__(self, attr, value):
        if attr == 'field1':
            self.__dict__[attr] = value
        else:
            raise AttributeError



class A:
def __init__(self, x):
self.__x = x
def __setattr__(self, attr, value):
if attr == "_A__x":
self.__dict__[attr] = value
else:
raise AttributeError


class WinDoor:
    def __init__(self, x, y):
        self.square = x * y


class Room:
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.wd = []
    def addWD(self, w, h):
        self.wd.append(WinDoor(w, h))
    def workSurface(self):
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        return new_square
r1 = Room(6, 3, 2.7)
print(r1.square) # выведет 48.6
r1.addWD(1, 1)
r1.addWD(1, 1)
r1.addWD(1, 2)
print(r1.workSurface()) # выведет 44.6