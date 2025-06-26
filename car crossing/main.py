import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)
car = CarManager()
player= Player()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
game_is_on = True

screen.listen()
screen.onkey(player.move,"Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.new_car_strip()
    for i in car.all_cars:
        i.backward(car.STARTING_MOVE_DISTANCE)
        if i.distance(player)<30:
            game_is_on=False
            scoreboard.game_is_over()
    if player.ycor()>280:
        game_is_on=False
        scoreboard.increase_level()
        player.go_to_start()
        time.sleep(1)
        game_is_on = True
        car.reset()
        car.increase_speed_of_cars()
screen.exitonclick()
