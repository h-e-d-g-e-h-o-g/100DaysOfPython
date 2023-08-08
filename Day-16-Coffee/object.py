from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkOrchid3")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
# With this attribute, we can get the canvas height of the my_screen object
# and the screen shows up and quickly disappear automatically when the program ends.
print(my_screen.exitonclick())
# With the help of this function, the screen is going to be shown up until we click on the screen
# means when we click on the screen, the screen disappears and program ends.
