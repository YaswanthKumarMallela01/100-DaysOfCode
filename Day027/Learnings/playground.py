"""Purpose: *args is used to pass a variable number of non-keyworded (positional)
arguments to a function.
Mechanism: When *args is used in a function definition, all the positional arguments
passed to the function are gathered into a tuple named args (or whatever name you choose
after the asterisk)."""


def add(*args):  # args stands for arguments. It is a tuple
    total = 0
    for n in args:
        total += n
    return total


print(add(2, 4, 6, 8, 10, 12, 14, 16, 18, 20))


'''Purpose: **kwargs is used to pass a variable number of keyworded arguments to a function.
Mechanism: When **kwargs is used in a function definition, all the keyword arguments passed 
to the function are gathered into a dictionary named kwargs (or whatever name you choose 
after the double asterisk). The keys of this dictionary are the keyword argument names, and
the values are their corresponding values.'''


def calculate(n, **kwargs):  # kwargs stands for keyword arguments. It is a dictionary
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=3, multiply=5))


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        '''kwargs[] give error if i missed even one argument value during creating of object.
        kwargs.get() returns 'None' even i missed 1 or more no of argument values'''


car = Car(make="Nissan", model="GT-R")
print(car.color)