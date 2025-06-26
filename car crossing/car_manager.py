from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10
    def new_car_strip(self):
        random_chance = random.randint(1,6)
        if random_chance ==1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-300, 300))
            self.all_cars.append(new_car)
    def reset(self):
        for c in self.all_cars:
            c.hideturtle()  # Hide the car
        self.all_cars.clear()  # Then clear the list
    def increase_speed_of_cars(self):
        self.STARTING_MOVE_DISTANCE+=self.MOVE_INCREMENT


