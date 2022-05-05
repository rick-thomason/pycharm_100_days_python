from turtle import Turtle
snake = Turtle(shape='square')


def move_forward():
    snake.forward(10)


def move_backwards():
    snake.backward(10)


def move_left():
    snake.left(10)


def move_right():
    snake.right(10)


def reset():
    snake.goto(-280, 0)

