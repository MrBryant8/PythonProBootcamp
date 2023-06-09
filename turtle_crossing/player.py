from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.seth(90)
        self.showturtle()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        self.goto(STARTING_POSITION)
        self.seth(90)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
