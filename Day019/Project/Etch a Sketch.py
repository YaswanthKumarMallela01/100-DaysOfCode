from turtle import Turtle, Screen

tim = Turtle()
tim.setheading(90)


def move_forward():
    tim.forward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)


def move_backward():
    tim.backward(10)


def clear():
    tim.clear()
    tim.penup()
    tim.goto(0, 0)
    tim.setheading(90)
    tim.pendown()


my_screen = Screen()
my_screen.listen()  # The function which listens to the keystrokes of your keyboard
'''A higher-order function is a function that either: 
Takes one or more functions as arguments, Returns a function as its result, 
and Does both of the above. '''
my_screen.onkey(fun=move_forward, key="w")  # Here onkey function is a higher order function.
my_screen.onkey(fun=move_left, key="a")
my_screen.onkey(fun=move_right, key="d")
my_screen.onkey(fun=move_backward, key="s")
my_screen.onkey(fun=clear, key="c")
my_screen.exitonclick()
