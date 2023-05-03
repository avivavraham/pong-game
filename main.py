from turtle import Screen
from score import ScoreBoard
from paddle import Paddle
from ball import Ball
import time
import math
import random
DEVIATION = 15
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
gap = 0
crash = False
while game_is_on:
    gap += 1
    if gap % 15 == 0:
        crash = False
    start_time = 0
    random_deviation = random.randint(-DEVIATION, DEVIATION)
    time.sleep(0.05)
    game_screen.update()
    ball.move()
    # detect collision with floor/ ceiling
    if (ball.ycor() > 260 or ball.ycor() < -260) and (not crash):
        crash = True
        gap = 15
        random_deviation = random.randint(-DEVIATION, DEVIATION)
        if 0 <= ball.heading() <= 90:
            ball.setheading(315 + random_deviation)
        elif 180 <= ball.heading() <= 270:
            ball.setheading(135 + random_deviation)
        elif 90 <= ball.heading() <= 180:
            ball.setheading(225 + random_deviation)
        else:
            ball.setheading(45 + random_deviation)
    # detect collisions with paddles
    if (((ball.xcor() - paddle1.xcor() <= 45) and (math.fabs(ball.ycor() - paddle1.ycor()) <= 65)) or
            ((paddle2.xcor() - ball.xcor() <= 45) and (math.fabs(ball.ycor() - paddle2.ycor()) <= 65)) and (not crash)):
        crash = True
        gap = 15
        random_deviation = random.randint(-DEVIATION, DEVIATION)
        ball.right(180 + random_deviation)
        ball.move_speed *= 1.1
    # detect collisions with the sides walls
        if ball.xcor() > 590:
            paddle1.goto((-575, 0))
            paddle2.goto((575, 0))
            ball.set_angle("right")
            score_player_1.score += 1
            if score_player_1.score >= 5:
                game_is_on = False
                score_player_1.game_over("left")
            score_player_1.score_update("left")
        elif ball.xcor() < -590:
            paddle1.goto((-575, 0))
            paddle2.goto((575, 0))
            ball.set_angle("left")
            score_player_2.score += 1
            if score_player_2.score >= 5:
                game_is_on = False
                score_player_2.game_over("right")
            score_player_2.score_update("right")

game_screen.exitonclick()
