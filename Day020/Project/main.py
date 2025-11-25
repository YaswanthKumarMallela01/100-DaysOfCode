from turtle import Turtle, Screen
import time
import snake

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("The Snake Game")
my_screen.tracer(0)

snake = snake.Snake()

my_screen.listen()
my_screen.onkey(fun=snake.up, key="Up")
my_screen.onkey(fun=snake.down, key="Down")
my_screen.onkey(fun=snake.left, key="Left")
my_screen.onkey(fun=snake.right, key="Right")

is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

my_screen.exitonclick()
