from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(3, 4)
v2 = Vector(6, 8)
v3 = v1 + v2
print(abs(v3))

#__repr__返回一个对象的字符串表示形式
#__add__和__mul__为类带来了+和*的算术运算
#默认情况下，我们自己定义的类的实例，总被认为是真的，除非这个类对于__bool__或者__len__函数有自己的实现。
#bool(x)背后调用的是x.__bool()的结果，如果不存在__bool__方法，会bool(x)会尝试调用x.__len__()，返回0，则bool会返回False
