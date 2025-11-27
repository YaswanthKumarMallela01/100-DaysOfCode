from turtle import Turtle


class Paddle(Turtle):  # Inheriting properties from Turtle class
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def go_up(self):
        """Makes the paddle go up when we press up key or w key"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Makes the paddle go down when we press down key or s key"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
