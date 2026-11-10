from functools import wraps


def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)

    return inner


@percent
@star
def printer(msg):
    print(msg)


printer("asdsad")
print(printer.__wrapped__.__wrapped__("asdasd"))
print(dir(printer))
