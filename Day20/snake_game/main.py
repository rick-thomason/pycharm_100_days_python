from turtle import Screen
from snake import Snake
import time

snake = Snake()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

screen.listen()
screen.onkey(key='Up', fun=snake.move_up)
screen.onkey(key='Down', fun=snake.move_down)
screen.onkey(key='Left', fun=snake.move_left)
screen.onkey(key='Right', fun=snake.move_right)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)

    snake.move()

screen.exitonclick()