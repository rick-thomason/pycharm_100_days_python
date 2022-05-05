from turtle import Turtle, Screen
import time

screen = Screen()
# screen.listen()
# screen.onkey(fun=move_forward, key='w')
# screen.onkey(fun=move_backwards, key='s')
# screen.onkey(fun=move_left, key='a')
# screen.onkey(fun=move_right, key='d')
# screen.onkey(fun=reset, key='c')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

segments = []

# create the 3 segments of starting snake
x_position = 0
for _ in range(3):
    new_segment = Turtle(shape='square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(x=x_position, y=0)
    x_position -= 20
    segments.append(new_segment)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)









screen.exitonclick()