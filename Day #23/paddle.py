from turtle import Turtle
DISTANCE = 20
UP = 90
DOWN = 270
PIECES = 5

class Paddle:
    def __init__(self, x_cor):
        #initialize an empty list
        self.pieces = []
        self.x_cor = x_cor
        self.body = self.create_body()
        self.head = self.body[0]

    def create_body(self):
        for num, piece in enumerate(['piece' for piece in range(PIECES)]):
            paddle = Turtle(shape='square')
            paddle.speed(0)
            paddle.penup()
            paddle.sety(num * -DISTANCE + 50)
            paddle.setx(self.x_cor)
            paddle.color('white')
            self.pieces.append(paddle)
        return self.pieces

    def up(self):
        self.body[0].seth(UP)
        for piece in range(len(self.body) - 1, 0, -1):
            new_x = self.body[piece - 1].xcor()
            new_y = self.body[piece - 1].ycor()
            self.body[piece].goto(new_x, new_y)
        self.body[0].forward(DISTANCE)

    def down(self):
        self.body[-1].seth(DOWN)
        for piece in range(0, len(self.body) - 1):
            new_x = self.body[piece + 1].xcor()
            new_y = self.body[piece + 1].ycor()
            self.body[piece].goto(new_x, new_y)
        self.body[-1].forward(DISTANCE)
