from turtle import Screen
from functions import move_forward, move_backwards, move_left, move_right, reset, snake

snake.color('white')
snake.penup()
snake.shapesize(stretch_len=3)

screen = Screen()
screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backwards, key='s')
screen.onkey(fun=move_left, key='a')
screen.onkey(fun=move_right, key='d')
screen.onkey(fun=reset, key='c')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')











screen.exitonclick()