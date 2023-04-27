from turtle import Turtle
FONT = ("Courier", 24, "bold")
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as f:
            self.high_score = int(f.read())
        self.penup()
        self.hideturtle()
        self.goto(-30, 260)
        self.pencolor('orange')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write("Score: {} High Score: {}".format(self.score, self.high_score), align=ALIGNMENT, font=FONT)

    def reset(self):
        global f
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


