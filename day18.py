import colorgram
from turtle import Screen

from day18_modules.super_turtle import SuperTurtle


turtle = SuperTurtle()

screen = Screen()
screen.colormode(turtle.colormode)

main_colors = colorgram.extract('./day18_files/spots.png', 16)
main_colors_list = [tuple(color.rgb) for color in main_colors if color.proportion <= 0.02]

turtle.paint_spots_picture(main_colors_list)

screen.exitonclick()
