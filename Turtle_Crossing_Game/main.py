import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
user = Player()
car_manager = CarManager()
score = Scoreboard()




screen.listen()
screen.onkey(user.movement, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for cars in car_manager.all_cars:
        if cars.distance(user)<20:
            score.game_over()
            game_is_on = False


    if user.is_at_finish():
        car_manager.level_up()
        score.increase_level()
        user.go_to_start()

screen.exitonclick()