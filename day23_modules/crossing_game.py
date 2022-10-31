import time

from turtle import Screen

from day23_modules.road import Road
from day23_modules.cross_turtle import CrossTurtle
from day23_modules.scoreboard import Scoreboard


class CrossingGame:
    DEFAULT_PARAMS = {
        'bg_color': 'white',
        'interface_color': 'black',
        'screen_height': 600,
        'screen_title': 'Yet another turtle challenge',
        'screen_width': 1200,
        'sleep_interval': 0.04,
        'sleep_interval_multiplier': 0.95,
        'turtle_color': 'green',
    }

    def __init__(self, screen: Screen, params=None):
        if not isinstance(params, dict):
            params = {}
        self.params = self.DEFAULT_PARAMS | params

        self.screen = screen
        self._setup_screen()

        self.road = Road(
            screen=self.screen,
            initial_speed=self.params['sleep_interval'],
            speed_multiplier=self.params['sleep_interval_multiplier']
        )
        self.cross_turtle = CrossTurtle(
            screen=self.screen,
            color=self.params['turtle_color']
        )
        self.scoreboard = Scoreboard(
            screen=self.screen,
            shift_x=0,
            shift_y=2 * self.cross_turtle.SEGMENT_SIZE,
            color=self.params['interface_color']
        )

        self.screen.listen()
        self._setup_events()

    def play(self):
        play_game = True
        while play_game:
            time.sleep(self.road.speed)
            self.road.move_cars(self.cross_turtle)

            if self.cross_turtle.road_is_crossed:
                self.cross_turtle.goto_start()
                self.scoreboard.add_level()
                self.road.increase_speed()

            if self.road.turtle_is_hit():
                self.scoreboard.game_over()
                play_game = False

            self.screen.update()

    def _setup_screen(self):
        self.screen.tracer(0)
        self.screen.setup(width=self.params['screen_width'], height=self.params['screen_height'])
        self.screen.bgcolor(self.params['bg_color'])
        self.screen.title(self.params['screen_title'])

    def _setup_events(self):
        self.screen.onkeypress(self.cross_turtle.move, 'Up')
