from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")

def cycle(degrees, sides):
    for i in range(sides):
        tim.right(degrees)
        tim.forward(50)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)

for i in range(3,9):
    change_color()
    degrees = int(360 / i)
    cycle(degrees, i)

screen = Screen()
screen.exitonclick()
