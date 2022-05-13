from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 270)
        self.write(f'Level: {self.level}', font=FONT, align=ALIGNMENT)

    def complete_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
