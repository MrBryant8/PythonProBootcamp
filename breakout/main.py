import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from obstacles import Obstacle

POSITIONS_Y = [100, 150, 200,  250]
TYPES = [("green", 0.9), ("yellow", 0.85), ("orange", 0.83), ("red", 0.8)]

game_is_on = True
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -250))
ball = Ball()

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")
obstacles = []

for y, (color, speed_boost) in zip(POSITIONS_Y, TYPES):
    for x in range(-360, 420, 100):
        obstacle = Obstacle((x, y), color, speed_boost)
        obstacles.append(obstacle)

while game_is_on:
    time.sleep(ball.speed_of_ball)
    screen.update()
    ball.move()

    # Detect if the ball went over
    if not (-380 < ball.xcor() < 380):
        ball.bounce_x()

    elif ball.ycor() > 280:
        ball.bounce_y()

    # Detect if ball hit paddles
    if ball.distance(paddle) < 50 and ball.ycor() < -220:
        ball.bounce_y()

    # Detect if the paddle missed the ball
    elif ball.ycor() < -300:
        ball.reset_position()
        ball.reset_speed()
        time.sleep(1)

    # Detect if paddle hits obstacle
    hit_obstacles = list(filter(lambda o: o.distance(ball) < 40, obstacles))
    if any(hit_obstacles) and (80 < ball.ycor() < 280):
        ball.bounce_y()
        ball.increase_speed(hit_obstacles[-1].speed_boost)
        hit_obstacles[-1].goto(-1000, -1000)

    # Detects if there are any obstacles left, if not quits game
    if len(list(filter(lambda o: o.position() == (-1000, -1000), obstacles))) == len(obstacles):
        game_is_on = False



