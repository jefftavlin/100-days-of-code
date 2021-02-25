from turtle import Turtle
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        #initialize an empty list
        self.snake_piece = []
        self.pieces = 3
        self.body = self.create_body()
        self.head = self.body[0]
        self.head.color('red')

    def create_body(self):
        for num, snake in enumerate(['piece' for piece in range(self.pieces)]):
            snake = Turtle(shape='square')
            snake.penup()
            snake.setx(num * -DISTANCE)
            snake.color('white')
            self.snake_piece.append(snake)
        return self.snake_piece

    def move(self):
        for piece in range(len(self.body) - 1, 0, -1):
            new_x = self.body[piece - 1].xcor()
            new_y = self.body[piece - 1].ycor()
            self.body[piece].goto(new_x, new_y)
        self.body[0].forward(DISTANCE)

    def extend(self):
        added_piece = Turtle(shape = 'square')
        added_piece.penup()
        added_piece.color('white')
        x = self.body[-1].xcor() - DISTANCE
        y = self.body[-1].ycor() - DISTANCE
        self.body.append(added_piece)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
