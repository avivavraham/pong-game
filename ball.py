from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__("circle")
        self.shapesize(1, 1, 1)
        self.color("white")
        self.penup()
        self.setheading(90)
        self.speed("slowest")
        self.move_speed = 1

    def set_angle(self, direction):
        self.goto((0, 0))
        self.move_speed = 1
        angle = random.randint(20, 170)
        if direction == "right":
            self.right(angle)
        else:
            self.left(angle)

    def move(self):
        self.forward(18 * self.move_speed)
