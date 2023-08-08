from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

is_game_on = True
scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        # Distance method is used to compare the distance from the turtle to the whatever passed into the paranthesis.
        food.refresh()
        snake.extend_segment()
        scoreboard.clear()
        scoreboard.score += 1
        scoreboard.score_update()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    for segment in snake.all_turtles[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()
