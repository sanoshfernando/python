import turtle
from turtle import Turtle,Screen
import random
tim = Turtle()
screen=Screen()
screen.colormode(255)
tim.speed("fastest")
for i in range(0,120):
    tim.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    tim.circle(100)
    tim.right(3)
screen.exitonclick()