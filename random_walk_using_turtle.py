import turtle
import random

timmy = turtle.Turtle()
turtle.colormode(255)
timmy.pensize(10)
distances = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for i in range(200):
    timmy.pencolor(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(distances))
