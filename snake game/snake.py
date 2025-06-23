from turtle import Turtle


MOVE_DISTANCE=10
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head= self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if int(self.head.heading())==0 :
            self.head.left(90)
        elif int(self.head.heading())==180:
            self.head.right(90)
    def down(self):
        if self.head.heading()==0 :
            self.head.right(90)
        elif self.head.heading()==180:
            self.head.left(90)
    def right(self):
        if self.head.heading()==270 :
            self.head.left(90)
        elif self.head.heading()==90:
            self.head.right(90)
    def left(self):
        if self.head.heading()==270 :
            self.head.right(90)
        elif self.head.heading()==90:
            self.head.left(90)
