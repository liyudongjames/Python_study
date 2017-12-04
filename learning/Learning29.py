# python中的private
# ‘_’和‘__’代表着私有，就是这么酷炫


def __say_some(name):
    print(name)


def _say_something(name):
    print(name)


def say_out_loud(name):
    if len(name) > 3:
        __say_some(name)
    else:
        _say_something(name)
