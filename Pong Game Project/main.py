from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("PONG GAME")
screen.bgcolor("black")

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=r_paddle.go_down, key="Down")

screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=l_paddle.go_down, key="s")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_x()

    if r_paddle.distance(ball) < 50 and ball.xcor() > 330:
        ball.bounce_y()

    elif l_paddle.distance(ball) < 50 and ball.xcor() < -330:
        ball.bounce_y()

    if ball.xcor() > 370:
        scoreboard.increase_l_score()
        scoreboard.update_scores()
        ball.home_ball()
        ball.reset_speed()

    elif ball.xcor() < -370:
        scoreboard.increase_r_score()
        scoreboard.update_scores()
        ball.home_ball()
        ball.reset_speed()

screen.exitonclick()
