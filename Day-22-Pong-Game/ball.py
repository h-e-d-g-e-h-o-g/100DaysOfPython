from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = 0.1

    # When the ball collides with the top wall then, bounce() will be called up, the y_move will be set to -10. Then,
    # the value of new_y will be decremented by 10 each time. But then, again it collides with the bottom wall, the
    # y_move will be set to again 10 by multiplying it yet again by -1.

