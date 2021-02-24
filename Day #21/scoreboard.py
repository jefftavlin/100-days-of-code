from turtle import Turtle
import random

FONT = ("Courier", 24, "normal")
x_cor = -200
y_cor = 250


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.goto(x_cor, y_cor)
        self.display_score()
        self.color('black')
        self.hideturtle()

    def display_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def update_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT)
