import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
POSITIONS = [(350, 0), (-350, 0)]

game_is_on = True
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(POSITIONS[0])
l_paddle = Paddle(POSITIONS[1])
ball = Ball()
sb = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


while game_is_on:
    time.sleep(ball.speed_of_ball)
    screen.update()
    ball.move()

    # Detect if the ball went over
    if not (-280 < ball.ycor() < 280):
        ball.bounce_y()

    # Detect if ball hit paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if the paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        sb.l_point()
        ball.reset_speed()
        time.sleep(1)

    elif ball.xcor() < -380:
        ball.reset_position()
        sb.r_point()
        ball.reset_speed()
        time.sleep(1)

    if sb.l_score == 10 or sb.r_score == 10:
        sb.game_over()
        game_is_on = False

screen.exitonclick()
