from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE
        self.starting_position = []
        self.all_car = []
        self.loop_car()

    def loop_car(self):
        for i in range(5):
            self.starting_position.append((random.randint(300, 330), random.randint(-200, 260)))

        for position in self.starting_position:
            self.create_car(position)

    def create_car(self, position):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setpos(position)
        self.all_car.append(new_car)

    def move_car(self):
        for random_car in self.all_car:
            random_car.setheading(180)
            random_car.forward(self.speed)

    def update_speed(self):
        self.speed += MOVE_INCREMENT
