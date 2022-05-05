from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet.', prompt='Which turtle will win the race? Enter a color: ').lower()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

y = -130
for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f'The winning color is {winning_color}. You win!')
            else:
                print(f'The winning color is {winning_color}... You suck!')

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
