from turtle import Turtle, Screen
import random
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

game = True
while game:
    screen.update()
    time.sleep(0.04)
    scoreboard.display_score()
    snake.move()

    # if snake hits fruit
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        game = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game = False
            scoreboard.game_over()

screen.exitonclick()
