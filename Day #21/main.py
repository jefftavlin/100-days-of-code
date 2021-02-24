import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score = Scoreboard()
p1 = Player()
cars = CarManager()

screen.listen()
screen.onkey(p1.up, 'w')
screen.onkey(p1.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.display_score()
    cars.move()
    positions = [car.position() for car in cars.cars if car.distance(p1.position()) < 23]

    if cars.loop_count % 6 == 0:
        cars.add_car()

    if len(positions) > 0:
        break

    if p1.ycor() >= 280:
        score.update_score()
        p1.lvl_up()
        cars.add_level()

score.game_over()
screen.exitonclick()
