from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        x_position = 0
        # create the 3 segments of starting snake
        for _ in range(3):
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(x=x_position, y=0)
            x_position -= 20
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
