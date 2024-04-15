from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.color("white")
        self.write(f"Score:{self.score}", False, align="center", font=("Arial", 18, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score:{self.score}", False, align="center",font=("Arial", 18, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align="center", font=("Arial", 18, "normal"))