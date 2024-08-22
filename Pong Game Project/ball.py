from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1, outline=1)
        self.x_cor = 10
        self.y_cor = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.y_cor *= -1
        self.ball_speed *= 0.9

    def bounce_y(self):
        self.x_cor *= -1
        self.ball_speed *= 0.9

    def home_ball(self):
        self.clear()
        self.home()
        self.move()

    def reset_speed(self):
        self.ball_speed = 0.1
