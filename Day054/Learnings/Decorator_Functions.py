import time

'''
def say_hello():
    time.sleep(2)
    print("Hello")


def say_by():
    time.sleep(2)
    print("Bye")
    
    
def say_greetings():
    time.sleep(2)
    print("How are you")
'''

"""Assigning same time.sleep(2) functionality to all the functions looks bad. Instead of we can
decorate the functions."""

# -------------------------------> Decorator Function

"""A decorator function is a function that takes another function as input and extends or 
modifies its behavior without changing its original code.
It uses functions as first-class objects and typically wraps additional logic around the target function.
Decorators enable clean separation of concerns and promote reusable, maintainable code."""


def decorator__function(function):
    def wrapper_class():
        time.sleep(2)
        function()
        function()
    return wrapper_class


@decorator__function
def say_hello():
    print("Hello")


@decorator__function
def say_bye():
    print("Bye")


@decorator__function
def say_greetings():
    print("How are you")


say_hello()
