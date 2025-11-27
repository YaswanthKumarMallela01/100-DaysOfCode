from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title("Pong")
my_screen.listen()
my_screen.tracer(0)

left_paddle = Paddle((-370, 0))
right_paddle = Paddle((370, 0))

ball = Ball()
scoreboard = Scoreboard()

'''Functional key design for right paddle'''
my_screen.onkey(fun=right_paddle.go_up, key="Up")
my_screen.onkey(fun=right_paddle.go_down, key="Down")
'''Functional key design for left paddle'''
my_screen.onkey(fun=left_paddle.go_up, key="w")
my_screen.onkey(fun=left_paddle.go_down, key="s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()

    '''Detecting collision with top and bottom walls'''
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    '''Detecting collisions with both left and right paddles'''
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340) or (ball.distance(left_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    '''Detecting if the paddle missed the ball or the ball went beyond the paddle on the right 
    side of the game screen'''
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    '''Detecting if the paddle missed the ball or the ball went beyond the paddle on the left 
    side of the game screen'''
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

my_screen.exitonclick()
