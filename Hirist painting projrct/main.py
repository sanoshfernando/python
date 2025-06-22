"""import colorgram
colors = colorgram.extract('image.jpg',30)
color_list=[]
for color in colors:
    color=color.rgb
    r = color[0]
    g = color[1]
    b = color[2]
    color_list.append((r,g,b))
print(color_list)"""
import turtle
from turtle import Turtle,Screen
import random
screen=Screen()
screen.colormode(255)


color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim = Turtle()

tim.speed("fastest")
for i in range(1,11):

    for j in range(0, 10):
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)
    tim.goto(0, i*50)



screen.exitonclick()
