from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.setheading(45)
        self.speed = 10

    def move(self):
        self.penup()
        self.forward(self.speed)
    def check_bounce(self):
        if self.ycor()>230 or self.ycor()<-230:
            if self.heading()>300 and self.ycor()<-220:
                self.setheading(self.heading()-270)
            elif self.heading()==135 and self.ycor()>220:
                self.setheading(self.heading()+90)
            else:
                self.setheading(self.heading()+270)
