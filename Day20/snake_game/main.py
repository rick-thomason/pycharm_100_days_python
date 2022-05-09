from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

screen.listen()
screen.onkeypress(key='Up', fun=snake.move_up)
screen.onkeypress(key='Down', fun=snake.move_down)
screen.onkeypress(key='Left', fun=snake.move_left)
screen.onkeypress(key='Right', fun=snake.move_right)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect if snake has run into food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect if snake has run into wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        is_game_on = False
        food.reset()
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_on = False
            food.reset()
            scoreboard.game_over()


screen.exitonclick()
