class StudentOne:

    count = 0

    def __init__(self, name):
        self.name = name
        StudentOne.count += 1

    def say_hello(self):
        print("hello world!I'm " + self.name)

    def what_is_your_name(self):
        print('my name is Lilei')
