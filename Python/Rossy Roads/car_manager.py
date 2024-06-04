import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.STARTING_MOVE_DISTANCE = 5


    def move(self):
        for car in self.cars:
            car.backward(self.STARTING_MOVE_DISTANCE)

    def next_level(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT


    def create(self):
        r = random.randint(1, 5)
        if r == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-200,250))
            self.cars.append(new_car)
        else:
            pass


















