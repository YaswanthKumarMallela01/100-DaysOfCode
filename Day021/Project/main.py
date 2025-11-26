from turtle import Screen
import time
import snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("The Snake Game")
my_screen.tracer(0)  # Turns off automatic screen updates

'''Creating snake, food and scoreboard objects'''
snake = snake.Snake()
food = Food()
score_board = Scoreboard()

'''Screen listens to the key strokes of your keyboard to move the snake up, down, left, right.
The functions(snake.up, snake.down, snake.left, snake.right) are defined in snake.py'''
my_screen.listen()
my_screen.onkey(fun=snake.up, key="Up")
my_screen.onkey(fun=snake.down, key="Down")
my_screen.onkey(fun=snake.left, key="Left")
my_screen.onkey(fun=snake.right, key="Right")

is_game_on = True
while is_game_on:
    my_screen.update()  # Used to explicitly refresh the screen when automatic updates are turned off using turtle.tracer(0)
    time.sleep(0.1)  # Used to pause the execution of a program for a specified duration
    snake.move()  # Function defined in snake.py

    if snake.head.distance(food) < 15:
        '''This 'if' block checks weather the head of the snake touches the randomly generated
        food or not. If the head touches the food, then the food goes to some other random location
        and the scoreboard increments with 1 and the snake extends as 10px as it eats more.'''
        food.refresh()
        score_board.increase_score()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        '''This 'if' block checks weather the head of the snake touches the corner of the game
        screen or not. If it touches then the game is over.'''
        is_game_on = False
        score_board.game_over()

    for segment in snake.segments[1:]:
        '''This loop checks weather the snake head is touching any part of it's own body or not.
        If yes then the game is over.'''
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score_board.game_over()

my_screen.exitonclick()
