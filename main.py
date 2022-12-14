from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong-game')
screen.tracer(1)

screen.listen()

l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(l_paddle.go_up, 's')
screen.onkey(l_paddle.go_down, 'x')
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.bounce_wall()
    ball.bounce_paddle(l_paddle)
    ball.bounce_paddle(r_paddle)
    ball.point(scoreboard)
    screen.update()
 
screen.exitonclick()