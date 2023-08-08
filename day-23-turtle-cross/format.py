from turtle import Turtle
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_segment(position)

    def add_snake_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.setpos(position)
        self.all_turtles.append(new_turtle)

    def extend_segment(self):
        self.add_snake_segment(self.all_turtles[-1].position())

    def move(self):
        for turtle_index in range(len(self.all_turtles) - 1, 0, -1):
            x_pos = self.all_turtles[turtle_index - 1].xcor()
            y_pos = self.all_turtles[turtle_index - 1].ycor()
            self.all_turtles[turtle_index].goto(x_pos, y_pos)
        self.all_turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
