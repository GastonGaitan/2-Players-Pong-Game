from turtle import Turtle
from scoreboard import Scoreboard
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('circle') # Change this by circle
        self.goto(0,-10)
        self.y_movement = 2
        self.x_movement = 10
        # self.speed(10)
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)
    
    def bounce_wall(self):
        if self.ycor() == 290 or self.ycor() == -280:
            self.y_movement *= -1

    def bounce_paddle(self, Paddle):
        if self.distance(Paddle) < 60:
            if self.xcor() == Paddle.xcor():
                self.x_movement = (self.x_movement * -1)
                # ball touches the lower side of the paddle.
                if self.ycor() < Paddle.ycor():
                    if self.y_movement > 0:
                        self.y_movement = (self.y_movement * -1)
                # If the ball touches the upper side of the paddle.
                elif self.ycor() > Paddle.ycor():
                    if self.y_movement < 0: 
                        self.y_movement = (self.y_movement * -1)
                self.move_speed *= 0.5
                print(self.move_speed)
                
    
    def restart(self):
        # New feature the ball will be returned into a random direction
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        random_movement = [1, -1]
        self.x_movement *= random.choice(random_movement)
        self.y_movement *= random.choice(random_movement)

    def point(self, scoreboard):
        if self.xcor() > 420:
            scoreboard.l_point()
            scoreboard.update_scoreboard()
            self.restart()

        elif self.xcor() < -420:
            scoreboard.r_point()
            scoreboard.update_scoreboard()
            self.restart()
    
    def increase_speed(self):
        self.bounce_count += 1
        if self.speed_atribute < 7 and self.bounce_count % 2 == 0:
            self.speed_atribute += 1
            # print("self.speed_atribute = ", self.speed_atribute)