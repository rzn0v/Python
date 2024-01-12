import turtle
import random

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def spirograph(gap_size):
    for i in range(int(360/gap_size)):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)

spirograph(5)

turtle.exitonclick()