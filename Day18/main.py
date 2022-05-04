from turtle import Screen, Turtle
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.speed(10)
timmy.pensize(3)

colors = ['medium aquamarine', 'dark orange', 'green', 'blue', 'purple', 'yellow', 'pink', 'brown']


# function to make the turtle form a square
def turtle_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)


# function to create a dashed line
def turtle_dash_line(num_dashes):
    for _ in range(num_dashes):
        timmy.pd()
        timmy.forward(10)
        timmy.pu()
        timmy.forward(10)


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side_n in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)


# turtle_square()
# turtle_dash_line(20)
screen = Screen()
screen.exitonclick()
