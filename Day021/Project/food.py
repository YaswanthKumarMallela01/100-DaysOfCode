from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        '''These are the characteristics of turtle which has been using by Food class'''
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Places the food in randomly generated places using x and y coordinates"""
        x_cor = random.randint(-270, 270)
        y_cor = random.randint(-270, 270)
        self.goto(x_cor, y_cor)