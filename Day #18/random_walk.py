from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")
tim.width(7)
tim.speed(7)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)

def walk():
    choices = [90,180,0,270]
    tim.seth(random.choice(choices))
    tim.forward(15)

for i in range(150):
    change_color()
    walk()

screen = Screen()
screen.exitonclick()
