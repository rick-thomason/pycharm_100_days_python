from turtle import Turtle


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.setheading(90)
        self.shapesize(stretch_wid=2, stretch_len=1)