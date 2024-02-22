from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}",align="center",font=("Arial",20,"normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over",align="center",font=("Arial",20,"normal"))

    def increment(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
        
        