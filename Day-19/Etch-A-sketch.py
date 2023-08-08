from turtle import Turtle, Screen

timmy = Turtle()


def move_forward():
    timmy.forward(20)


def move_backward():
    timmy.backward(20)


def move_counterclockwise():
    timmy.left(10)


def move_clockwise():
    timmy.right(10)


def clear_the_screen():
    timmy.setpos(0, 0)
    timmy.setheading(0)
    timmy.clear()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_the_screen)

screen.exitonclick()
