from turtle import Turtle

ALIGNMENT = "center"
L_ALIGNMENT = "left"
R_ALIGNMENT = "right"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(x=-110, y=260)
        self.write(f"{self.l_score}", align=L_ALIGNMENT, font=FONT)

        self.goto(x=110, y=260)
        self.write(f"{self.r_score}", align=L_ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score += 1

    def increase_r_score(self):
        self.r_score += 1
