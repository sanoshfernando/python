from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
x=-230
y=-100
is_game_on=True
bet=screen.textinput("Betting Window","Chose a color").lower()

colors=["red","orange","green","blue","yellow","purple"]
all_turtles=[]
for color in colors:
    new_turtle="tim"+color
    new_turtle = Turtle()
    new_turtle.color(color)
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(x, y)
    y+=50
    all_turtles.append(new_turtle)
while is_game_on:
    for one_turtle in all_turtles:
        if one_turtle.xcor()>230:
            is_game_on=False
            winner=one_turtle
            w_color = one_turtle.pencolor()
            if w_color ==bet:
                print(f"The winner is {w_color} You won")
            else:
                print(f"The winner is {w_color} You lost")
        else:
            one_turtle.forward(random.randint(0,15))

screen.exitonclick()
