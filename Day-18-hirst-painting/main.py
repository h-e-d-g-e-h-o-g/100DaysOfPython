import turtle as t
import random

t.colormode(255)
# import colorgram
# color_set = colorgram.extract('painting.jpg', 30)
# color_list = []
# for color_object in color_set:
#     rgb_object = color_object.rgb
#     r = rgb_object.r
#     g = rgb_object.g
#     b = rgb_object.b
#     color_item = (r, g, b)
#     color_list.append(color_item)
color_list = [(246, 242, 235), (247, 240, 244), (239, 242, 247), (237, 245, 240), (212, 149, 95), (215, 80, 62),
              (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29),
              (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96),
              (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63),
              (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]

timmy = t.Turtle()
timmy.speed("fastest")
timmy.setheading(225)
timmy.penup()
timmy.hideturtle()
timmy.forward(300)
timmy.pendown()


def draw_dot():
    for j in range(9):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    timmy.dot(20, random.choice(color_list))
    timmy.penup()
    timmy.setheading(90)
    timmy.forward(50)


for i in range(1, 11):
    if i % 2 != 0:
        timmy.setheading(0)
    else:
        timmy.setheading(180)
    draw_dot()

screen = t.Screen()
screen.exitonclick()
