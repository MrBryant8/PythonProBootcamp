import time
from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

player = Player()
car_manager = CarManager()
sb = Scoreboard()
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
iterations = 0
while game_is_on:

    time.sleep(0.1)
    screen.update()
    
    #
    for car in car_manager.cars:
        if car.distance(player) < 20:
            sb.game_over()
            game_is_on = False

    # Detect successful finish
    if player.is_at_finish_line():
        player.level_up()
        car_manager.car_speed += 1
        sb.player_level += 1
        sb.update_scoreboard()

    # Create a car every six iterations
    if iterations % 6 == 0:
        car_manager.create_car()

    car_manager.move()
    iterations += 1

screen.exitonclick()