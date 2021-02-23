from turtle import Turtle, Screen

class Setup(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor('black')
        self.screen.tracer(0)
        self.screen.title('Pong')
        self.line()

    def line(self):
        for i in range(19):
            self.screen.tracer(0)
            line = Turtle('square')
            line.speed(0)
            line.penup()
            line.color('black')
            line.goto(0, 280 - (i * 30))
            line.shapesize(0.5, 0.3, 0.5)
            line.color('white')

    def update(self):
        self.screen.update()

    def exit(self):
        self.screen.exitonclick()

    def onkey(self,func, key):
        self.screen.listen()
        self.screen.onkey(func, key)
    def quit(self):
        self.screen.bye()
