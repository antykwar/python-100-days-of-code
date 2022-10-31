import time

from turtle import Screen

from .message_writer import MessageWriter
from .snake import Snake
from .food import Food


class SnakeGame:
    SLEEP_TIME = {'slow': 1, 'normal': 0.5, 'fast': 0.1}
    DEFAULT_PARAMS = {
        'bg_color': 'black',
        'messages_color': 'white',
        'messages_slot': 'top',
        'snake_color': 'white',
        'snake_length': 3,
        'screen_title': 'Legendary snake game',
        'screen_height': 800,
        'screen_width': 800,
        'shift_for_snake_field': 30,
        'sleep_time': 'normal'
    }

    def __init__(self, screen: Screen, params=None):
        if not isinstance(params, dict):
            params = {}
        self.params = self.DEFAULT_PARAMS | params

        self.screen = screen
        self.screen.tracer(0)
        self.screen.setup(width=self.params['screen_width'], height=self.params['screen_height'])
        self.screen.bgcolor(self.params['bg_color'])
        self.screen.title(self.params['screen_title'])

        self.snake = Snake(color=self.params['snake_color'], length=self.params['snake_length'], screen=self.screen)
        self.food = Food(screen=self.screen)
        self.message_writer = MessageWriter(
            self.screen,
            slot=self.params['messages_slot'],
            color=self.params['messages_color']
        )

        self.screen.listen()
        self.screen.onkeypress(self.snake.turn_left, 'Left')
        self.screen.onkeypress(self.snake.turn_right, 'Right')

        self.score = 0
        self.high_score = 0
        self._init_high_score()

    def play(self):
        self._update_score()
        self._give_food()

        stop_game = False
        while True:
            self.snake.move_forward()

            if self.snake.can_eat_food(self.food):
                self.score += 1
                self._update_score()
                self._give_food()
                self.snake.grow_up()

            if self.snake.has_boarder_collision(self._get_allowed_snake_field()) or self.snake.has_self_collision():
                self._game_over()
                stop_game = True

            self.screen.update()
            if stop_game:
                break

            self._slow_down()

    def _update_score(self):
        self.message_writer.write_message(f'Your score is: {self.score}. Current high score is {self.high_score}.')

    def _game_over(self):
        message = f'Game over. Your score is: {self.score}.'
        if self.score > self.high_score:
            self.high_score = self.score
            message += ' New high score!'
            self._save_high_score()
        self.message_writer.write_message(message)

    def _slow_down(self):
        time.sleep(self.SLEEP_TIME[self.params['sleep_time']])

    def _give_food(self):
        self.food.appear_randomly(
            margin_top=self.message_writer.get_height_on_screen() + 2 * self.snake.SEGMENT_SIZE
        )

    def _get_allowed_snake_field(self):
        return {
            'x_min': -(self.screen.window_width() / 2 - self.params['shift_for_snake_field']),
            'x_max': self.screen.window_width() / 2 - self.params['shift_for_snake_field'],
            'y_min': -(self.screen.window_height() / 2 - self.params['shift_for_snake_field']),
            'y_max': self.screen.window_height() / 2 - self.message_writer.get_height_on_screen(),
        }

    def _init_high_score(self):
        try:
            with open('day20_21_files/high_score.txt', 'r') as reader:
                high_score = reader.readline()
                self.high_score = int(high_score) if high_score else 0
        except FileNotFoundError:
            self.high_score = 0

    def _save_high_score(self):
        try:
            with open('day20_21_files/high_score.txt', 'w') as writer:
                writer.write(str(self.high_score))
        except PermissionError:
            pass
