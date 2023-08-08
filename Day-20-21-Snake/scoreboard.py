from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')
with open("../../OneDrive/Desktop/high_score.txt", "r") as f:
    high = f.read()
    high = int(high)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.high_score = high
        self.score = 0
        self.score_update()

    def score_update(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            str_high = str(self.high_score)
            with open("high_score.txt", "w") as file:
                file.write(str_high)
        self.clear()
        self.score = 0
        self.score_update()

