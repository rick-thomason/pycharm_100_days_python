from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

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
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with right paddle
    if ball.xcor() > 340 and ball.distance(right_paddle) < 50:
        ball.hit_paddle()

    # Detect collision with left paddle
    if ball.xcor() < -340 and ball.distance(left_paddle) < 50:
        ball.hit_paddle()

screen.exitonclick()
