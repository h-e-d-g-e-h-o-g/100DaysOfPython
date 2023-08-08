from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-280, 260)
        self.level = 1
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(f" Level : {self.level}", align=ALIGNMENT, font=FONT)

    def update_level(self):
        self.level += 1
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
