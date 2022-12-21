from turtle import Turtle

PADDLE_LENGTH = 5
PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"
PADDLE_SPEED = 40


class Paddle(Turtle):

    def __init__(self, start_position, screen_height):
        super().__init__()
        self.screen_half_height = screen_height / 2
        self.start_position = start_position
        self.color(PADDLE_COLOR)
        self.shape(PADDLE_SHAPE)
        self.shapesize(PADDLE_LENGTH, 1, 1)
        self.penup()
        self.goto(x=self.start_position, y=0)

    def move_up(self):
        if self.ycor() < (self.screen_half_height - 60):
            self.goto(x=self.xcor(), y=self.ycor() + PADDLE_SPEED)

    def move_down(self):
        if self.ycor() > -(self.screen_half_height - 60):
            self.goto(x=self.xcor(), y=self.ycor() - PADDLE_SPEED)
