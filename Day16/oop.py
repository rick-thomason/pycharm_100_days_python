# Object Oriented Programming

# Constructing Objects
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column('Pokemon Name', ['Pikachu', 'Charmander', 'Squirtle'])
table.add_column('Type', ['Electric', 'Fire', 'Water'])

table.align = 'l'


print(table)


