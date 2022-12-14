from turtle import Turtle, Screen

# This first class is used to create both a playable
# paddle or a one that will be used by the machine
# the one that is playable will have methods to move itself

class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.x_position = x_position
        self.goto(x_position, 0)
        self.score = 0

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

        
# class Paddle_Player(Paddle):
#     def __init__(self, x_position):
#         super().__init__(x_position)
    
#     def go_up(self):
#         new_y = self.ycor() + 20
#         self.goto(self.xcor(), new_y)

#     def go_down(self):
#         new_y = self.ycor() - 20
#         self.goto(self.xcor(), new_y)



