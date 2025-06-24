from turtle import Turtle

def dashed_line():
    tim = Turtle()
    tim.color("white")
    tim.penup()
    tim.width(5)
    tim.speed("fastest")
    tim.goto(0, -235)
    tim.left(90)
    for _ in range(0, 10):
        tim.pendown()
        tim.forward(25)
        tim.penup()
        tim.forward(25)
    tim.hideturtle()

class Dashboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def score_board(self):
        self.clear()  # 👈 clears previous text
        self.goto(100, 150)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.goto(-100, 150)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

    def r_win(self):
        self.r_score += 1
        self.score_board()  # 👈 refreshes both scores

    def l_win(self):
        self.l_score += 1
        self.score_board()  # 👈 refreshes both scores
