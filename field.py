from turtle import Turtle

BAR_SIZE = 10
COLOR = "white"
FONT = ('Arial', 30, 'normal')


class Field(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.color(COLOR)
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=screen_height/2)
        self.right(90)
        for x in range(int(screen_height / BAR_SIZE * 2)):
            self.pendown()
            self.fd(BAR_SIZE)
            self.penup()
            self.fd(BAR_SIZE)
