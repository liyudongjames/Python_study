# Learning 11 __特殊方法__

from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    # 如果向量的模为0那么这个向量就为假
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


vector1 = Vector(2, 3)
vector2 = Vector(4, 2)
print(vector1)
vector3 = vector1 + vector2
print(abs(vector2))
print(vector1*2)
print(bool(vector1))
vector4 = Vector(0, 0)
print(bool(vector4))
