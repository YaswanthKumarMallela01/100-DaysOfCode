"""functions are treated as first-class citizens and can be passed as arguments to other functions.
Here, calculate() accepts another function as a parameter and executes it dynamically,
enabling clean, modular, and highly scalable logic reuse."""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculate(operator_function, n1, n2):
    return operator_function(n1, n2)


print(calculate(multiply, 5, 10))
print(calculate(add, 5, 10))
print(calculate(subtract, 5, 10))
print(calculate(divide, 5, 10))

# -------------------> Nested Functions


def outer():
    print("I'm Outer")

    def inner():
        print("I'm Inner")
    inner()


outer()

# ----------------------> Functions can be returned from another function


def fun1():
    print("I am fun1")

    def fun2():
        print("I am fun2")
    return fun2


'''When fun1 is called it returns fun2. We can store return from fun1 to a variable and 
can call explicitly.'''
nested_function = fun1()  # fun2 is returned
nested_function()
