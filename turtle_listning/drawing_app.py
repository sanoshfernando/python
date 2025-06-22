from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.forward(10)
def backward():
    tim.backward(10)
def c_rotate():
    tim.right(10)
def cc_rotate():
    tim.left(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(forward, "w")
screen.onkeypress(backward, "s")
screen.onkeypress(c_rotate, "a")
screen.onkeypress(cc_rotate, "d")
screen.onkeypress(clear, "a")

screen.exitonclick()
