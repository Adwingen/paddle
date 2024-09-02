from turtle import Turtle

COLOR = "white"
POSITION = (0, 0)
MOVE = 10
MOVE_SPEED = 0.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(COLOR)
        self.shapesize(1, 1)
        self.penup()
        self.goto(POSITION)
        self.move_x = MOVE
        self.move_y = MOVE
        self.move_speed = MOVE_SPEED

    def ball_move(self):
        new_y = self.ycor() + self.move_y
        new_x = self.xcor() + self.move_x
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = MOVE_SPEED

    def bounce_x(self):
        self.move_x *= -1
        self.color("red")

    def bounce_y(self):
        self.move_y *= -1
        self.color("blue")

    def resetBall(self):
        self.shape("circle")
        self.color(COLOR)
        self.shapesize(1, 1)
        self.penup()
        self.goto(POSITION)
        self.move_x = MOVE
        self.move_y = MOVE
        self.move_speed = MOVE_SPEED
