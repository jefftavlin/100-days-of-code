from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")
tim.width(0.5)
tim.speed(12)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)

for i in range(250):
    change_color()
    tim.circle(100)
    tim.left(i)
    tim.forward(1)

screen = Screen()
screen.exitonclick()
