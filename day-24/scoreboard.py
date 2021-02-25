from turtle import Turtle
import random

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = [0]
        self.goto(0, 245)
        self.display_score()
        self.color('white')
        self.hideturtle()
    def display_score(self, max_high_score = 0):
        self.clear()
        self.write(f"Score: {self.score} - High Score: {max_high_score}", align="center", font = ('Arial', 24, 'normal'))
    def update_score(self):
        self.score +=1
        self.highscore.append(self.score)
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font = ('Arial', 24, 'normal'))
    def high_score(self):
        self.high = max(self.highscore)
        return self.high
