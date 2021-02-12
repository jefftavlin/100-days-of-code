from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.color('black')

for i in range(15):
    tim.forward(4)
    tim.penup()
    tim.forward(4)
    tim.pendown()

screen = Screen()
screen.exitonclick()
