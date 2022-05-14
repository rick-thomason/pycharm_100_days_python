import pandas as pd
import turtle

states = pd.read_csv('50_states.csv')
image = 'blank_states_img.gif'

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.addshape(image)

turtle.shape(image)


screen.exitonclick()






