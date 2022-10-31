import time

from turtle import Screen

from .paddle import Paddle
from .ball import Ball
from .net_drawer import NetDrawer
from .scoreboard import Scoreboard


class PongGame:
    DEFAULT_PARAMS = {
        'ball_color': 'yellow',
        'bg_color': 'black',
        'interface_color': 'white',
        'paddle_length': 5,
        'screen_title': 'Legendary pong game',
        'screen_height': 600,
        'screen_width': 600,
        'score_shift_x': 50,
        'score_shift_y': 50,
        'sleep_interval': 0.04,
        'speed_multiplier': 0.95
    }

    def __init__(self, screen: Screen, params=None):
        if not isinstance(params, dict):
            params = {}
        self.params = self.DEFAULT_PARAMS | params

        self.screen = screen
        self._setup_screen()

        self.left_paddle = self._setup_paddle('left')
        self.right_paddle = self._setup_paddle('right')

        self.scoreboard = Scoreboard(self.screen, self.params['score_shift_x'], self.params['score_shift_y'])

        self.ball = Ball(
            self.screen,
            initial_speed=self.params['sleep_interval'],
            speed_multiplier=self.params['speed_multiplier'],
            color=self.params['ball_color']
        )

        self.net_drawer = NetDrawer()
        self._setup_net()

        self.screen.listen()
        self._setup_events()

    def play(self):
        while True:
            time.sleep(self.ball.speed)
            self.ball.move()
            self.ball.check_paddle_hit(self.left_paddle)
            self.ball.check_paddle_hit(self.right_paddle)
            side_with_point = self.ball.check_success_side(
                (self.left_paddle.get_back_line_for_ball(), self.right_paddle.get_back_line_for_ball())
            )
            if side_with_point:
                self.scoreboard.add_point(side_with_point)
            self.screen.update()

    def _setup_screen(self):
        self.screen.tracer(0)
        self.screen.setup(width=1200, height=800)
        self.screen.bgcolor(self.params['bg_color'])
        self.screen.title(self.params['screen_title'])

    def _setup_paddle(self, position):
        return Paddle(
            color=self.params['interface_color'],
            length=self.params['paddle_length'],
            screen=self.screen,
            position=position
        )

    def _setup_events(self):
        self.screen.onkeypress(self.left_paddle.up, 'w')
        self.screen.onkeypress(self.left_paddle.down, 's')
        self.screen.onkeypress(self.right_paddle.up, 'Up')
        self.screen.onkeypress(self.right_paddle.down, 'Down')

    def _setup_net(self):
        self.net_drawer.color(self.params['interface_color'])
        self.net_drawer.goto(0, -(self.screen.window_height() / 2))
        self.net_drawer.setheading(90)
        self.net_drawer.dashed_line(length=self.screen.window_height(), strip_size=20, gap_size=10)
