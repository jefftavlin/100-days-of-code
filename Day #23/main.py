from turtle import Turtle, Screen
import random
import time
from scoreboard import Scoreboard
from setup import Setup
from paddle import Paddle
from ball import Ball

screen = Setup()
player_1_score = Scoreboard(-100)
player_2_score = Scoreboard(100)
p1_paddle = Paddle(350)
p2_paddle = Paddle(-350)
ball = Ball()

screen.onkey(p1_paddle.up, 'Up')
screen.onkey(p1_paddle.down, 'Down')
screen.onkey(p2_paddle.up, 'w')
screen.onkey(p2_paddle.down, 's')

screen.onkey(screen.quit, 'q')
game = True

while game:
    screen.update()
    ball.move()
    player_1_score.display_score()
    player_2_score.display_score()
    x_cor_p1 = [(piece.xcor() - 10, piece.ycor() - 10) for piece in p1_paddle.body]
    x_cor_p2 = [(piece.xcor() + 10, piece.ycor() + 10) for piece in p2_paddle.body]

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.position() in x_cor_p1 or ball.position() in x_cor_p2:
        ball.rebound()

    if ball.xcor() > 380:
        player_1_score.update_score()
        ball.restart()
    elif ball.xcor() < - 380:
        player_2_score.update_score()
        ball.restart()

screen.exit()
