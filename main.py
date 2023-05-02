from turtle import Screen
from score import ScoreBoard
from paddle import Paddle
from ball import Ball
import time
import math
# TODO: fix ball stack agents paddle bug
# settings of screen
game_screen = Screen()
game_screen.setup(width=1200, height=600)
game_screen.bgcolor("black")
game_screen.title("My Pong Game")
game_screen.tracer(0)
score_player_1 = ScoreBoard("left")
score_player_2 = ScoreBoard("right")
score_player_1.score_update("left")
score_player_2.score_update("right")
score_player_1.set_partition()
paddle1 = Paddle((-575, 0))
paddle2 = Paddle((575, 0))
ball = Ball()
game_screen.listen()
game_screen.onkeypress(paddle1.up, "Up")
game_screen.onkeypress(paddle2.up, "w")
game_screen.onkeypress(paddle1.down, "Down")
game_screen.onkeypress(paddle2.down, "s")
game_is_on = True
ball.set_angle("right")
while game_is_on:
    time.sleep(0.06)
    game_screen.update()
    ball.move()
    # detect collision with floor/ ceiling
    if ball.ycor() > 285 or ball.ycor() < -285:
        if 0 <= ball.heading() <= 90 or 180 <= ball.heading() <= 270:
            ball.right(90)
        elif 0 <= ball.heading() <= 180:
            ball.left(90)
        else:
            ball.setheading(45)
    # detect collisions with paddles
    if ((math.dist(ball.position(), paddle1.position()) < 45) and ball.xcor() < -550) or\
            ((math.dist(ball.position(), paddle2.position()) < 45) and ball.xcor() > 550):
        ball.right(180)
game_screen.exitonclick()

