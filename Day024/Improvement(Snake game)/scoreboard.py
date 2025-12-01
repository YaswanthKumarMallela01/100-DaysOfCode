from turtle import Turtle
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):  # Had to mention from where you wanted to inherit characteristics. (Turtle)
    def __init__(self):
        super().__init__()  # Scoreboard Inherits characteristics from turtle class
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        '''These are the characteristics of turtle which has been using by scoreboard class'''
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=FONT)

    """Deleted game_over function and added reset function to play continuously till
    you click stop button."""
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
