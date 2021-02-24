from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
DISTANCE = 20
PIECES = 2


class CarManager():
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = self.create_cars()
        self.loop_count = 0

    def create_car(self):
        self.car = Turtle(shape='square')
        self.car.penup()
        self.car.shapesize(1, 2)
        self.car.sety(random.randint(-250, 250))
        self.car.setx(random.randint(320, 700))
        self.car.color(random.choice(COLORS))
        self.car.seth(180)
        return self.car

    def create_cars(self):
        self.cars = []
        for i in range(25):
            car = self.create_car()
            self.cars.append(car)
        return self.cars

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)
            self.loop_count += 1

    def add_level(self):
        self.move_distance += MOVE_INCREMENT

    def add_car(self):
        self.cars.append(self.create_car())
