from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.title('Pong')
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(fun=left_paddle.move_up, key='w')
screen.onkey(fun=left_paddle.move_down, key='s')
screen.onkey(fun=right_paddle.move_up, key='Up')
screen.onkey(fun=right_paddle.move_down, key='Down')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()