from turtle import Turtle
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):  # Had to mention from where you wanted to inherit characteristics. (Turtle)
    def __init__(self):
        super().__init__()  # Scoreboard Inherits characteristics from turtle class
        self.score = 0
        '''These are the characteristics of turtle which has been using by scoreboard class'''
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
