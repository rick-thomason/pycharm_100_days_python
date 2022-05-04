from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.color('medium aquamarine')
timmy.pensize(15)
timmy.speed(0)  # fastest speed

colors = ['medium aquamarine', 'dark orange', 'green', 'blue', 'purple', 'yellow', 'pink', 'brown']
directions = [0, 90, 180, 270]

for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(50)
    timmy.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()