from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Paddle Game")
screen.tracer(0)

scoreboard = Scoreboard()
paddle_one = Paddle((250, 10))
paddle_two = Paddle((-250, 10))
ball = Ball()


for i in range(-280, 280, 40):
    red_table = Turtle()
    red_table.shape("square")
    red_table.color("white")
    red_table.penup()
    red_table.goto(x=0, y=i)
  


screen.listen()

screen.onkey(paddle_one.up, "Up")
screen.onkey(paddle_one.down, "Down")


game_on = True


while game_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.display_scoreboard()
    paddle_one.move()
    ball.move()


    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()

    
    #if ball.xcor() > 250 or ball.xcor() < -250:
    #    ball.hit_paddle()
    
    if ball.xcor() > 280:
        scoreboard.score_aumented_one()
        ball.restart()

    elif ball.xcor() < -280:
        scoreboard.score_aumented_two()
        ball.restart()



screen.exitonclick()