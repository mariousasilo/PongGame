from turtle import Turtle


BAR_SIZE = 10
COLOR = "white"
FONT = ('Courier', 30, 'normal')


class Scoreboard(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.color(COLOR)
        self.hideturtle()
        self.penup()
        self.goto(x=x_cor, y=y_cor)
        self.score = 0
        self.write(arg=f"{self.score}", align="center", font=FONT)

    def record(self):
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}", align="center", font=FONT)
