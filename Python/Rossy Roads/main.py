import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# creating object scoreboard
score = Scoreboard()

# creating object screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# creating object car manager
car = CarManager()


# creating object turtle
turtle = Player()

# setupting the movements
screen.listen()
screen.onkey(turtle.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()
    for i in car.cars:
        if i.distance(turtle) < 25:
            screen.clear()
            score.game_over()
            time.sleep(3)
            game_is_on = False
        else:
            pass
    if turtle.ycor() > 300:
        turtle.next_level()
        score.increase()
        car.next_level()













