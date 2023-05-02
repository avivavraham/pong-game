from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 40, 'normal')

'''
score board class-
responsible for keep tracking of the score, and displaying it constantly.
responsible to displaying GAME OVER when the user loses.
'''


class ScoreBoard(Turtle):
    def __init__(self, direction):
        super(ScoreBoard, self).__init__()
        self.score = 0
        self.penup()
        if direction == "left":
            self.goto((-300, 235))
        else:
            self.goto((300, 235))
        self.color("white")
        self.hideturtle()

    def score_update(self, direction):
        if direction == "left":
            self.write(f"{self.score}", align=direction, font=FONT)
        else:
            self.write(f"{self.score}", align=direction, font=FONT)

    def set_partition(self):
        partition = super()
        partition.hideturtle()
        partition.penup()
        partition.goto((0, 290))
        partition.setheading(270)
        while partition.ycor() > -290:
            partition.pendown()
            partition.forward(10)
            partition.penup()
            partition.forward(10)

    def game_over(self):
        self.goto((0, 0))
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
