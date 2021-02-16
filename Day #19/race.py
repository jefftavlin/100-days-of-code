from turtle import Turtle, Screen
import random

race = False
screen = Screen()
screen.setup(width = 500, height = 400)
bet = screen.textinput("Make your bet", 'Which turtle will win the race? Enter a color: ')
colors = ['red','orange','yellow','green','blue','purple']
turtles = []

for num, color in enumerate(colors):
    turtle = Turtle(shape = 'turtle')
    turtle.color(color)
    turtle.penup()
    turtle.goto(x = -230, y = (120 - num * 40))
    turtles.append(turtle)

if bet:
    race = True

while race:
    for turtle in turtles:
        distance = random.randint(0,10)
        turtle.forward(distance)
        if turtle.xcor() > 230:
            race = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The winning color is {winning_color}.")
            else:
                print(f"You've lost! The winning color is {winning_color}")

screen.listen()
screen.exitonclick()
