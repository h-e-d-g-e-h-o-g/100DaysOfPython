from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
game_is_on = True
scoreboard = Scoreboard()
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
    elif ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()


    # else:
    #     ball.collision_wall()
    #     straight_move = False
    #     if ball.ycor() < -300:
    #         straight_move = True  my_solution by using flag
screen.exitonclick()
