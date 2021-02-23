from turtle import Turtle
import random
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('white')
        self.y_move = 10
        self.x_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        time.sleep(0.05)

    def bounce(self):
        self.y_move *= -1

    def rebound(self):
        self.x_move *= -1

    def restart(self):
        self.goto(0,0)
