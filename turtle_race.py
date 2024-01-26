from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
game_on = False
colors = ["red", "blue", "green", "black", "purple", "cyan"]

bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
all_turtle=[]
y = -100
x = -230
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x, y )
    y = y+50
    all_turtle.append(new_turtle)

if bet:
    game_on = True

while game_on:
    for turtle in all_turtle:
        if turtle.xcor()> 230:
            game_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle won.")
            else:
                print(f"You've lost! The {winning_color} turtle won.")
        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()



