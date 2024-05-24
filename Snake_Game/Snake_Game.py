from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoring = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        scoring.increment()
        snake.extend()
        food.refresh()

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() >290 or snake.segments[0].ycor() <-290:
        scoring.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<10:
            scoring.reset()
            snake.reset()
        
screen.exitonclick()