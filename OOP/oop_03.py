# __slots__限制属性，对子类没有效果


class Car:
    __slots__ = "name", "speed"


car = Car()
# 动态绑定属性
car.name = "sdfs"
car.speed = "120"
# 下面 car.color会报如下错误
# Traceback (most recent call last):
#  File "E:/Python/python_study/OOP/oop_03.py", line 12, in <module>
#   car.color = "white"
# AttributeError: 'Car' object has no attribute 'color'
car.color = "white"

