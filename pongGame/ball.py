import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed_of_ball = 0.1
        self.speed(self.speed_of_ball)
        self.circle(40)
        self.penup()
        self.color("orange")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed_of_ball *= 0.9

    def reset_position(self):
        self.home()
        self.bounce_x()

    def reset_speed(self):
        self.speed_of_ball = 0.1


