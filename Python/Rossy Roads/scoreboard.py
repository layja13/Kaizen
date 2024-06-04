from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("black")
        self.goto(-290, 260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,20)
        self.write("GAME OVER", align="center", font=FONT)
        self.goto(0, -20)
        self.write(f"Final score: {self.score}", align="center", font=FONT)


