from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

screen.listen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.back(10)

def turn_left():
    timmy.setheading(timmy.heading()+10)

def turn_right():
    timmy.setheading(timmy.heading()-10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
