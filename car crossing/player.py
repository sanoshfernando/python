STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.speed("fastest")
        self.go_to_start()
        self.left(90)
    def move(self):
        self.forward(MOVE_DISTANCE)
    def go_to_start(self):
        self.goto(STARTING_POSITION)