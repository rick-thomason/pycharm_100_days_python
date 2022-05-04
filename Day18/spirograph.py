import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed(0)


def gen_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


pensize = list(range(0, 11))


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.pensize(random.choice(pensize))
        timmy.color(gen_random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(10)

screen = turtle.Screen()
screen.exitonclick()
