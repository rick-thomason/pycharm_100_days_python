# import colorgram

# Extract 6 colors from an image.
# colors = colorgram.extract('hirst.jpg', 30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import turtle
import random

timmy = turtle.Turtle()
turtle.colormode(255)
timmy.speed(0)
timmy.penup()
timmy.hideturtle()

color_list = [(208, 160, 79), (46, 188, 119), (227, 50, 81), (107, 201, 112), (55, 103, 165), (236, 239, 246),
              (201, 45, 29), (189, 46, 101), (104, 110, 182), (220, 127, 145), (42, 173, 189), (97, 178, 199),
              (24, 135, 106), (41, 45, 124), (197, 12, 31), (18, 100, 82), (206, 165, 25), (185, 24, 20),
              (152, 216, 154), (232, 170, 188), (221, 219, 16), (17, 21, 81), (235, 171, 162), (185, 185, 210),
              (5, 69, 55)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(30, random.choice(color_list))
    timmy.fd(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle.Screen()
screen.exitonclick()