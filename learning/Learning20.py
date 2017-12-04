# 装饰器


def log(text):
    def detector(func):
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return detector


@log("Li")
def before():
    print("I used to be a good guy. Then life fuck me")


before()
