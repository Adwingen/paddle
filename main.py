from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from menu import Menu
import random
import time


# Configurações e inicializações
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Variável para armazenar o modo de jogo
game_mode = None
MAX_SCORE = 5


# Função para exibir o menu inicial
menu = Menu()


# Função para reiniciar o jogo
def restart_game():
    screen.clear()
    screen.bgcolor("black")
    menu.display_menu()

    # Variável global para o modo de jogo
    global game_mode
    game_mode = None

    # Definir as teclas para seleção do modo de jogo
    screen.listen()
    screen.onkeypress(select_single_player, "1")
    screen.onkeypress(select_two_players, "2")

    # Loop para esperar a seleção do usuário
    while game_mode is None:
        screen.update()

    # Iniciar o jogo com o modo selecionado
    start_game()


# Funções para selecionar o modo de jogo
def select_single_player():
    global game_mode
    game_mode = "single"


def select_two_players():
    global game_mode
    game_mode = "two"


# Função principal do jogo
def start_game():
    screen.clear()
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)

    paddle_right = Paddle((350, 0))
    paddle_left = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()
    game_is_on = True

    # Configuração de controles para o paddle esquerdo
    screen.listen()
    screen.onkeypress(paddle_left.go_up, "w")
    screen.onkeypress(paddle_left.go_down, "s")
    screen.onkeyrelease(paddle_left.stop, "w")
    screen.onkeyrelease(paddle_left.stop, "s")

    # Configuração de controles para o paddle direito no modo de 2 jogadores
    if game_mode == "two":
        screen.onkeypress(paddle_right.go_up, "Up")
        screen.onkeypress(paddle_right.go_down, "Down")
        screen.onkeyrelease(paddle_right.stop, "Up")
        screen.onkeyrelease(paddle_right.stop, "Down")

    # Função para movimentação do computador
    paddle_right.computer_move(paddle_right, ball)

    # Verificar se há vencedor
    def check_winner():
        if scoreboard.l_score >= MAX_SCORE:
            display_restart_screen("Left Player")
            return True
        elif scoreboard.r_score >= MAX_SCORE:
            display_restart_screen("Right Player")
            return True
        return False


    # Tela de reinício
    def display_restart_screen(winner):
        screen.clear()
        screen.bgcolor("black")
        screen.title("Pong Game")

        message = f"{winner} Wins!\nPress 'r' to Restart or 'q' to Quit"
        restart_screen = Turtle()
        restart_screen.color("white")
        restart_screen.hideturtle()
        restart_screen.penup()
        restart_screen.goto(0, 0)
        restart_screen.write(message, align="center", font=("Courier", 24, "normal"))

        screen.listen()
        screen.onkeypress(restart_game, "r")
        screen.onkeypress(screen.bye, "q")

        while True:
            screen.update()

    # Loop principal do jogo
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.ball_move()

        # Movimentação dos paddles
        paddle_right.move()
        paddle_left.move()

        if game_mode == "single":
            paddle_right.computer_move(paddle_right, ball)

        # Verificar colisões e atualizar placar
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(paddle_right) < 50 and ball.xcor() > 320:
            ball.bounce_x()
            ball.move_speed *= 0.85

        if ball.distance(paddle_left) < 50 and ball.xcor() < -320:
            ball.bounce_x()
            ball.move_speed *= 0.85

        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.l_point()
            if check_winner():
                game_is_on = False

        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.r_point()
            if check_winner():
                game_is_on = False


# Iniciar o jogo pela primeira vez
restart_game()







