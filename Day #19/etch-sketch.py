from turtle import Turtle, Screen
import random

# w = forward
#a = left
#d = right
#s = backwards

tim = Turtle()

def move_forwards():
    tim.forward(15)

def move_left():
    tim.left(15)

def move_right():
    tim.right(15)

def move_back():
    tim.backward(15)

def clear():
    tim.clear()
    tim.reset()

screen = Screen()
screen.listen()

screen.onkey(key = 'w', fun = move_forwards)
screen.onkey(key = 'a', fun = move_left)
screen.onkey(key = 'd', fun = move_right)
screen.onkey(key = 's', fun = move_back)
screen.onkey(key = 'c', fun = clear)

screen.exitonclick()
