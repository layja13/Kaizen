from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_one = 0
        self.score_two = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.color("white")
        self.display_scoreboard()
    

    def score_aumented_one(self):
        self.score_one += 1
        self.display_scoreboard()


    def score_aumented_two(self):
        self.score_two += 1
        self.display_scoreboard()
    

    def display_scoreboard(self):
        self.clear()
        self.write(f"{self.score_one} | {self.score_two}", align=ALIGNMENT, font=FONT, )


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over", font=FONT, align=ALIGNMENT)
