from turtle import Screen

from day19_modules.turtle_race import TurtleRace


screen = Screen()
screen.setup(width=500, height=400)
supposed_winner = screen.textinput(
    title='Your choice',
    prompt='Enter the color of turtle who as you think will come first'
)

turtle_race = TurtleRace(screen)
turtle_race.init_turtles(6)

turtle_race.perform_race()
turtle_race.announce_race_result(supposed_winner)

screen.exitonclick()
