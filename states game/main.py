import turtle
import pandas
from pandas import read_csv

image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

data = read_csv("50_states.csv")
states = data.state.to_list()
guessed_count=0

def answer():
    global guessed_count,ans
    ans = turtle.textinput(title=f"{guessed_count}/50 States correct", prompt="Name another state").title()
    if ans in states:
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        state_data = data[data.state == ans]
        writer.goto(state_data.x.item(), state_data.y.item())
        writer.write(state_data.state.item())
        states.remove(ans)
        guessed_count+=1

while len(states)!=0:
    answer()
    if ans == "Exit":
        break
missing_states = pandas.DataFrame(states)
missing_states.to_csv("states_to_learn.csv")
