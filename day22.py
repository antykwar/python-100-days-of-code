from turtle import Screen

from day22_modules.pong_game import *


screen = Screen()

pong_game = PongGame(screen)
pong_game.play()

screen.exitonclick()
