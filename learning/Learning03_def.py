from learning.Leaning02 import use_me


def say_hello(name, age):
    print("My name is " + name.title() + ", I'm " + str(age) + " years old!")


say_hello('david', 12)
say_hello(name='ace', age='32')
say_hello(age=14, name='jack')

use_me('hello')



