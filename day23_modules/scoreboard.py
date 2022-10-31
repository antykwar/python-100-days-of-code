from .message_writer import MessageWriter


class Scoreboard:
    def __init__(self, screen, shift_x, shift_y, color):
        self.screen = screen
        self.shift_x = shift_x
        self.shift_y = shift_y
        self.level = 1
        self.score = MessageWriter(screen, color=color)
        self.result = MessageWriter(screen, color=color)
        self._setup_score()

    def add_level(self):
        self.level += 1
        self._update_score()

    def game_over(self):
        self.result.write_message('GAME OVER')

    def _setup_score(self):
        y_position = self.screen.window_height() / 2 - self.shift_y
        self.score.goto(0, y_position)
        self.result.goto(0, 0)
        self._update_score()

    def _update_score(self):
        self.score.write_message(f'Level {str(self.level)}')
