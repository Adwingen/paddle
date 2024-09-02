from turtle import Turtle
import random

COLOR = "white"
MOVE = 20  # Ajuste a velocidade de movimento se necessário


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color(COLOR)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.move_direction = 0  # Direção de movimento: 1 para cima, -1 para baixo, 0 parado

    def go_up(self):
        self.move_direction = 1

    def go_down(self):
        self.move_direction = -1

    def stop(self):
        self.move_direction = 0

    def move(self):
        new_y = self.ycor() + MOVE * self.move_direction
        if -250 < new_y < 250:  # Limites para evitar que o paddle saia da tela
            self.goto(self.xcor(), new_y)

    def computer_move(Self, paddle_right, ball):
        if random.random() > 0.675:
            return

        move_step = random.randint(10, 20)

        if paddle_right.ycor() < ball.ycor() and abs(paddle_right.ycor() - ball.ycor()) > 10:
            paddle_right.goto(paddle_right.xcor(), paddle_right.ycor() + move_step)
        elif paddle_right.ycor() > ball.ycor() and abs(paddle_right.ycor() - ball.ycor()) > 10:
            paddle_right.goto(paddle_right.xcor(), paddle_right.ycor() - move_step)
        else:
            paddle_right.stop()



