from turtle import Turtle, Screen
import random
import colorgram

tim = Turtle()
tim.speed(12)

screen = Screen()
screen.colormode(255)
screen.setup(550, 620)

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
#
# print(rgb_colors)

color_list = [(150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

print(tim.pos())

def change_color():
    choice = random.choice(color_list)
    tim.color(choice)

tim.penup()
tim.setx(-190)
tim.sety(-220)
tim.pendown()

for i in range(11):
    for i in range(10):
        change_color()
        tim.dot(20)
        tim.penup()
        tim.forward(40)
    tim.setx(-190)
    tim.sety(tim.pos()[1] + 50)
    tim.penup()

screen.exitonclick()
