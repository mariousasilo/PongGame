import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from field import Field
from ball import Ball


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
half_width = SCREEN_WIDTH / 2
half_height = SCREEN_HEIGHT / 2
screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong: The Famous Arcade Game")

screen.tracer(0)
field = Field(SCREEN_HEIGHT)
ball = Ball()
paddle_left = Paddle(start_position=-(half_width - 40), screen_height=SCREEN_HEIGHT)
paddle_right = Paddle(start_position=half_width - 40, screen_height=SCREEN_HEIGHT)
score_left = Scoreboard(x_cor=-50, y_cor=half_height - 50)
score_right = Scoreboard(x_cor=50, y_cor=half_height - 50)

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() >= half_height - 20 or ball.ycor() <= -(half_height - 20):
        ball.border_bounce()
    elif ball.distance(paddle_left) < 50 and ball.xcor() == -(half_width - 60):
        ball.paddle_bounce()
    elif ball.distance(paddle_right) < 50 and ball.xcor() == (half_width - 60):
        ball.paddle_bounce()
    elif ball.xcor() <= -half_width:
        score_right.record()
        ball.reset()
    elif ball.xcor() >= half_width:
        score_left.record()
        ball.reset()

    screen.listen()
    screen.onkeypress(fun=paddle_left.move_up, key="w")
    screen.onkeypress(fun=paddle_left.move_down, key="s")
    screen.onkeypress(fun=paddle_right.move_up, key="Up")
    screen.onkeypress(fun=paddle_right.move_down, key="Down")

screen.exitonclick()
