from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_count = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 240)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level_count}", font=FONT, align="left")

    def increase_level(self):
        self.level_count += 1
        self.update_score()

    def game_is_over(self):
        self.goto(0,0)
        self.write("Game Over", font=FONT, align="center")

