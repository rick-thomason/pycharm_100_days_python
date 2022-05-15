from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f'{self.l_score}', font=FONT, align=ALIGNMENT)
        self.goto(100, 200)
        self.write(f'{self.r_score}', font=FONT, align=ALIGNMENT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
