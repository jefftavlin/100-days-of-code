from turtle import Turtle
import random

class Setup(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.title('Pong')

    def line(self):
        for i in range(19):
            line = Turtle('square')
            line.speed(20)
            line.penup()
            line.goto(0, 280 - (i * 30))
            line.shapesize(0.5, 0.3, 0.5)
            line.color('white')
