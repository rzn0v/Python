from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}",align="center",font=("Arial",20,"normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def increment(self):
        self.score+=1
        self.update_scoreboard()
        
        