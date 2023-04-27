import random
import turtle
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = 0

    def create_car(self):
        car = turtle.Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.goto(280, random.randint(-230, 250))
        self.cars.append(car)

    def move(self):
        for n in range(len(self.cars)):
            self.cars[n].backward(STARTING_MOVE_DISTANCE + (self.car_speed * MOVE_INCREMENT))