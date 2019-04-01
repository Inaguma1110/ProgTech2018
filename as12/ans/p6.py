class Trapezoid:
    def __init__(self, u, l, h):
        self.u = u
        self.l = l
        self.h = h

    def area(self):
        return (self.u + self.l) * self.h // 2


class Square(Trapezoid):
    def __init__(self, w):
        super().__init__(w, w, w)


a = int(input())
s = Square(a)
print(s.area())
