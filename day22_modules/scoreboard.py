from .message_writer import MessageWriter


class Scoreboard:
    def __init__(self, screen, shift_x, shift_y):
        self.screen = screen
        self.shift_x = shift_x
        self.shift_y = shift_y
        self.score = {'left': 0, 'right': 0}
        self.left_score_pad = MessageWriter(self.screen)
        self.right_score_pad = MessageWriter(self.screen)
        self._setup_score()

    def add_point(self, side_with_point):
        self.score[side_with_point] += 1
        self._update_score()

    def _setup_score(self):
        y_position = self.screen.window_height() / 2 - self.shift_y
        self.left_score_pad.goto(-1 * self.shift_x, y_position)
        self.right_score_pad.goto(self.shift_x, y_position)
        self._update_score()

    def _update_score(self):
        self.left_score_pad.write_message(str(self.score['left']))
        self.right_score_pad.write_message(str(self.score['right']))
