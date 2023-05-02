from turtle import Screen
from score import ScoreBoard
from paddle import Paddle

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
game_screen.update()
game_screen.exitonclick()

