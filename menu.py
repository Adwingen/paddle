from turtle import Turtle


class Menu(Turtle):
    def __init__(self):
        super().__init__()
        self.display_menu()


    def display_menu(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 100)
        self.write("PONG GAME", align="center", font=("Courier", 36, "normal"))
        self.goto(0, 0)
        self.write("Pressione '1' para 1 Jogador\nPressione '2' para 2 Jogadores", align="center",
                   font=("Courier", 24, "normal"))

    def display_winner(self, winner):
        self.clear()
        self.color("white")
        self.goto(0, 50)
        self.write(f"{winner} Wins!", align="center", font=("Courier", 36, "normal"))
        self.goto(0, -50)
        self.write("Press 'r' to Restart or 'q' to Quit", align="center", font=("Courier", 24, "normal"))

