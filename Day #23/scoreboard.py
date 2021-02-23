from turtle import Turtle
import random

class Scoreboard(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.score = 0
        self.goto(xcor, 225)
        self.display_score()
        self.color('white')
        self.hideturtle()

    def display_score(self):
        self.clear()
        self.write(f"{self.score}", align="center", font = ('Arial', 48, 'normal'))
        
    def update_score(self):
        self.score +=1

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font = ('Arial', 48, 'normal'))
