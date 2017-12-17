# 元类


class Hello(object):

    def hello(self, name="world"):
        print("name, %s" %name)


my = Hello()
my.hello()
print(type(my))


def copy_some():
    print("use this funtion")


# 运用type动态创建一个类（动态语言的特点）
# 函数和类的定义不是在编译的时候定义，而是在运行时动态创建的
car = type("Car", (object,), dict(say=copy_some, name="Benz"))
car.say()
print(car.name)

# 元类 metaclass

