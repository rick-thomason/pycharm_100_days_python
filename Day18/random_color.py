import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.pensize(20)
timmy.speed(0)  # fastest speed

directions = [0, 90, 180, 270]


def gen_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(200):
    timmy.color(gen_random_color())
    timmy.forward(40)
    timmy.setheading(random.choice(directions))


screen = turtle.Screen()
screen.exitonclick()
