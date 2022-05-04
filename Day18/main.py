from turtle import Screen, Turtle

timmy = Turtle()
timmy.color('dark orange')
timmy.shape('turtle')
timmy.speed(2.5)


# function to make the turtle form a square
def turtle_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)


def turtle_dash_line():
    for _ in range(10):
        timmy.pd()
        timmy.forward(10)
        timmy.pu()
        timmy.forward(10)


# turtle_square()
turtle_dash_line()
screen = Screen()
screen.exitonclick()
