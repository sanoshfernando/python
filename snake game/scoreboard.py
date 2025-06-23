from turtle import Turtle,Screen



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score: {self.score}",False,"center",("Arial",24,"normal"))

    def game_over(self):
        self.clear()
        self.write("GAME OVER",False,"center",("Arial",24,"normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

