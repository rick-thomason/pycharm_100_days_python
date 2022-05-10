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

speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    # Detect collision with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.bounce_x()

    # Detect if ball goes past right paddle
    if ball.xcor() > 380:
        ball.reset_position()

    # Detect if ball goes past left paddle
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()
