from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.body = []
        self.create_paddle(position)
        self.head = self.body[0]
        self.head.setheading(0)
        self.is_moving = False

    
    def create_paddle(self, position):
        for i in range(1,6):
            paddle_part = Turtle()
            paddle_part.shape("square")
            paddle_part.penup()
            paddle_part.color("white")
            paddle_part.goto(x=position[0], y=position[1] + i*20)
            self.body.append(paddle_part)

        
    
    def move(self):
        if self.is_moving:
            if self.head.heading() == 270:
                for body_part in range(0, len(self.body) - 1):
                    new_x = self.body[body_part + 1].xcor()
                    new_y = self.body[body_part + 1].ycor()
                    
                    self.body[body_part].goto(x=new_x, y=new_y)

            elif self.head.heading() == 90:
                for body_part in range(len(self.body) - 1, 0, -1):
                    new_x = self.body[body_part - 1].xcor()
                    new_y = self.body[body_part - 1].ycor()
                    
                    self.body[body_part].goto(x=new_x, y=new_y)
                
            self.head.forward(20)


    def up(self):
        if self.head.heading() != 90 or self.is_moving != True:
            self.head = self.body[0]
            self.head.setheading(90)
            self.is_moving = True


    def down(self):
        if self.head.heading() != 270 or self.is_moving != True:
            self.head = self.body[-1]
            self.head.setheading(270)
            self.is_moving = True
