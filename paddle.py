from turtle import Turtle
MOVE_QUANTITY = 20
'''
paddle class-
responsible for creating paddles
responsible for moving the paddles up and down.
'''


class Paddle(Turtle):
    def __init__(self, location):
        super(Paddle, self).__init__("square")
        self.shapesize(4, 0.3, 4)
        self.color("white")
        self.penup()
        self.goto(location)
        self.showturtle()


