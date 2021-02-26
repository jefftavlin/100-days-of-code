from turtle import Turtle
import pandas as pd

class Game:
    def __init__(self, df, state_answer):
        self.df = df
        self.state_answer = state_answer
        self.x, self.y = self.get_x_y()
        self.place_on_map()

    def get_x_y(self):
        self.df = self.df[self.df.state == self.state_answer]
        x = self.df['x'].values[0]
        y = self.df['y'].values[0]
        return x, y

    def place_on_map(self):
        state = Turtle()
        state.penup()
        state.hideturtle()
        state.goto(self.x, self.y)
        state.write(self.state_answer)
