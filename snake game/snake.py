from turtle import Turtle


MOVE_DISTANCE=10
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.color("white")
            new_segment.shape("square")
            new_segment.goto(i)
            self.segments.append(new_segment)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)


    def up(self):
        if int(self.segments[0].heading())==0 :
            self.segments[0].left(90)

        elif int(self.segments[0].heading())==180:
            self.segments[0].right(90)

    def down(self):
        if self.segments[0].heading()==0 :
            self.segments[0].right(90)
        elif self.segments[0].heading()==180:
            self.segments[0].left(90)
    def right(self):
        if self.segments[0].heading()==270 :
            self.segments[0].left(90)
        elif self.segments[0].heading()==90:
            self.segments[0].right(90)
    def left(self):
        if self.segments[0].heading()==270 :
            self.segments[0].right(90)
        elif self.segments[0].heading()==90:
            self.segments[0].left(90)
