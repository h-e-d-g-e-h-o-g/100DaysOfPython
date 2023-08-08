import time
from turtle import Screen
from player import Player
import random
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(fun=player.upward, key="Up")
game_is_on = True
scoreboard = Scoreboard()
car = CarManager()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_car()

    if car.all_car[-2].xcor() < 270:
        car.create_car((random.randint(300, 330), random.randint(-200, 260)))

    if player.ycor() == 280:
        scoreboard.update_level()
        car.update_speed()
        player.goto(0, -280)

    for check in car.all_car:
        if player.distance(check) < 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
