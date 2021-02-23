from turtle import Turtle, Screen
import random
import time
from scoreboard import Scoreboard
from setup import Setup
from paddle import Paddle

screen = Setup()
player_1_score = Scoreboard(-100)
player_2_score = Scoreboard(100)
p1_paddle = Paddle(350)
p2_paddle = Paddle(-350)

screen.onkey(p1_paddle.up, 'Up')
screen.onkey(p1_paddle.down, 'Down')
game = True

while game:
    screen.update()
    player_1_score.display_score()
    player_2_score.display_score()
    time.sleep(0.1)

screen.exit()
