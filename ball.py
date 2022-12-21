from turtle import Turtle


COLOR = "red"
SHAPE = "circle"
DISTANCE = 20
ANGLES = [45, 135, 225, 315]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.color(COLOR)
        self.seth(135)
        self.x_position = self.xcor()
        self.y_position = self.ycor()
        self.x_distance = DISTANCE
        self.y_distance = DISTANCE
        self.move_speed = 0.1

    def move(self):
        self.x_position += self.x_distance
        self.y_position += self.y_distance
        self.goto(self.x_position, self.y_position)

    def border_bounce(self):
        self.y_distance *= -1

    def paddle_bounce(self):
        self.x_distance *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.home()
        self.x_position = self.xcor()
        self.y_position = self.ycor()
        self.x_distance *= -1
        self.move_speed = 0.1
