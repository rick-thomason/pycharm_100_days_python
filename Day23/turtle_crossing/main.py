from turtle import Screen
from player import Player
from car import Car
import time

leo = Player()
car = Car()

screen = Screen()
screen.title('Turtle Crossing')
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkeypress(fun=leo.move, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()

