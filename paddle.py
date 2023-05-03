from turtle import Turtle
MOVE_QUANTITY = 25
'''
paddle class-
responsible for creating paddles
responsible for moving the paddles up and down.
'''


class Paddle(Turtle):
    def __init__(self, location):
        super(Paddle, self).__init__("square")
        self.setheading(90)
        self.shapesize(0.2, 4, 3)
        self.color("white")
        self.penup()
        self.goto(location)
        self.speed("fastest")
        self.showturtle()

    def up(self):
        self.setheading(90)
        self.forward(MOVE_QUANTITY)

    def down(self):
        self.setheading(270)
        self.forward(MOVE_QUANTITY)
