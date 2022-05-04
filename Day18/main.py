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


turtle_square()

screen = Screen()
screen.exitonclick()
