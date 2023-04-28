from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def left(self):
        x_cor = self.xcor() - 50
        self.goto(x_cor, self.ycor())

    def right(self):
        x_cor = self.xcor() + 50
        self.goto(x_cor, self.ycor())
