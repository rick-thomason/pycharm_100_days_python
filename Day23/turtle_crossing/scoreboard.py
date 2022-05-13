from turtle import Turtle

ALIGNMENT = 'left'
FONT = ('Courier', 24, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-290, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT, align=ALIGNMENT)

    def complete_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)
