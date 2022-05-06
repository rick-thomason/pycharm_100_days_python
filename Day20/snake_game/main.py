from turtle import Screen
from snake import Snake
import time

snake = Snake()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)

    snake.move()

screen.exitonclick()