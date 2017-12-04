# python中的面向对象


class Legendary(object):

    def __init__(self):
        pass

    def __init__(self, name, what):
        self.name = name
        self.what = what

    def say(self):
        print(self.name + " " + self.what + " is LEGENDARY")


me = Legendary("Li", "Monkey King")
me.say()
