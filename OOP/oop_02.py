# 高级面向对象编程
# 方法绑定
from types import MethodType


class Student:

    def __init__(self, name):
        self.name = name


def set_name(self, name):
    self.name = name


stu = Student("Mary")
print(stu.name)
# 利用MethodType进行方法绑定,但是这种办法绑定的方法只对这一个实例有用
stu.set_name = MethodType(set_name, stu)
stu.set_name("David")

print(stu.name)

# 这种方法的方法绑定对所有实例都有效果
Student.set_name = set_name
