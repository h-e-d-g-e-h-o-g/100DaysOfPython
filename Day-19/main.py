from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which color will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
x = -230
y = -100
count = 0
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for one_turtle in all_turtles:
        if one_turtle.xcor() > 230:
            winner_color = one_turtle.pencolor()
            if user_bet == winner_color:
                print(f"You've won. The {winner_color} is the winner.")
            else:
                print(f"You've lost. The {winner_color} is the winner.")
            is_race_on = False

        random_distance = random.randint(0, 10)
        one_turtle.forward(random_distance)

screen.exitonclick()
