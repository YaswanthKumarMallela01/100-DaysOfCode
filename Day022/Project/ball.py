from turtle import Turtle


class Ball(Turtle):  # Inheriting properties from Turtle class
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Make the ball move linearly with the increase of both x and y coordinates by 10px"""
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        """When the collision detected with top or bottom of the screen, the y coordinates will
        change to negative as the ball should move in opposite direction"""
        self.y_move *= -1

    def bounce_x(self):
        """When the collision detected with left or right of the screen, the x coordinates will
        change to negative as the ball should move in opposite direction"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """This function is triggered when the ball misses one side of paddle and went beyond
        the paddle to the right or left side of the screen"""
        self.goto(0, 0)
        self.bounce_x()
