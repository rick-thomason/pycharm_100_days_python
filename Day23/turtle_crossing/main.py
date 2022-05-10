from turtle import Screen
from player import Player
from car_manager import CarManager
import time

screen = Screen()
screen.title('Turtle Crossing')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()


screen.listen()
screen.onkeypress(fun=player.move, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect if turtle collides with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False

screen.exitonclick()
