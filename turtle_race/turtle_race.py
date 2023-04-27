from turtle import *
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.title("Turtle race")
screen.setup(500, 400)
user_balance = 100

while user_balance >= 10:
    screen.clear()
    list_of_turtles = []
    for i in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(-240, (30 * i))
        list_of_turtles.append(new_turtle)

    user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color:")
    user_bet_price = screen.numinput("Make your bet", "Minimum bet is $10.\nHow much $ are you going to bet?",
                                     minval=10.0)

    if user_bet and user_bet_price:
        is_race_on = True
        user_balance -= user_bet_price

        while is_race_on:
            for turtle in list_of_turtles:
                if turtle.xcor() > 230:
                    winning_color = turtle.pencolor()
                    is_race_on = False
                    if winning_color == user_bet:
                        penup()
                        hideturtle()
                        goto(-30, -100)
                        write("Congratulations, you've won!\nThe winner is the {} turtle."
                              .format(winning_color), align="center", font=("Cooper Black", 10, "italic"))
                        user_balance += user_bet_price * 6
                    else:
                        penup()
                        hideturtle()
                        goto(-30, -100)
                        write("A shame, you've lost!\nThe winner is the {} turtle, while you bet on the {} one."
                              .format(winning_color, user_bet), align="center", font=("Cooper Black", 10, "italic"))
                    break
                rand_distance = random.randint(0, 10)
                turtle.forward(rand_distance)

    user_answer = screen.textinput("Play again?", "Do you wanna play again?\nYour current balance is ${}."
                                   .format(user_balance))
    if user_answer == "no":
        break


screen.exitonclick()
