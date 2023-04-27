from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
sb = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, 'w')
screen.onkey(snake.move_down, 's')
screen.onkey(snake.move_left, 'a')
screen.onkey(snake.move_right, 'd')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if food.distance(snake.head) < 15:
        sb.increment_score()
        snake.extend()
        food.move()

    # Detect collision with wall
    if not ((-290 < snake.head.xcor() < 290) and (-290 < snake.head.ycor() < 290)):
        # sb.game_over()
        # game_is_on = False
        sb.reset()
        snake.reset()


    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # sb.game_over()
            sb.reset()
            snake.reset()

screen.exitonclick()
