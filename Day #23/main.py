from turtle import Turtle, Screen
import random
import time
from scoreboard import Scoreboard
from setup import Setup

screen = Setup()

screen.tracer(0)
screen.listen()

player_1_score = Scoreboard(-100)
player_2_score = Scoreboard(100)

game = True

screen.exitonclick()
