# Closures

"""
Defining a Python Closure Function: Closure in Python is an inner function object,
a function that behaves like an object, that remembers and has access to variables
in the local scope in which it was created even after the outer function has finished executing.


Closure in Python is an inner function object, a function that behaves like an object,
that remembers and has access to variables in the local scope in which it was created
even after the outer function has finished executing.

"""


def greeting(name):
    def message(msg):
        return f"{name} - {msg}"

    return message


msg_for_boris = greeting("Boris")
msg_for_kirill = greeting("Kirill")

print(msg_for_boris("Go to home!"))
print(msg_for_boris("Go to work!"))
print(msg_for_kirill("Do it!"))
print(msg_for_kirill("Go to sleep"))


def discount_factory(percent):
    def apply(price):
        saving = round(price * percent / 100, 2)
        return round(price - saving, 2)
    return apply


black_friday = discount_factory(30)
vip = discount_factory(15)
employee = discount_factory(40)

cart = [120.00, 45.50, 200.00, 89.99]

print("Black Friday:", [black_friday(p) for p in cart])
print("VIP:         ", [vip(p) for p in cart])
print("Employee:    ", [employee(p) for p in cart])
