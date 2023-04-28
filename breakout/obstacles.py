from turtle import Turtle


class Obstacle(Turtle):
    def __init__(self, position, color, speed_boost):
        super().__init__()
        self.color(color)
        self.shape("square")
        self.resizemode("user")
        self.speed_boost = speed_boost
        self.shapesize(stretch_wid=2, stretch_len=4, outline=1)
        self.penup()
        self.goto(position)
