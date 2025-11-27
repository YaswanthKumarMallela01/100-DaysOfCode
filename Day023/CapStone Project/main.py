import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = ScoreBoard()

my_screen.listen()
my_screen.onkey(fun=player.go_up, key="Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    my_screen.update()
    '''Creates cars in random places and moves by 10px'''
    car_manager.create_cars()
    car_manager.move_car()

    '''Checking if any car hits the turtle or not'''
    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            is_game_on = False
            score_board.game_over()

    '''Checking if turtle reaches the other end which is a finish line'''
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()


my_screen.exitonclick()
