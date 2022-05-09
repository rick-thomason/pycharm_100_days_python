from turtle import Turtle
import random

COLOR = 'yellow'


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color(COLOR)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-250, 280)
        self.goto(x=random_x, y=random_y)