import turtle

from .states_explorer import StatesExplorer
from .message_writer import MessageWriter


class StatesGame:
    DEFAULT_PARAMS = {
        'coordinates_delta': 10,
        'screen_title': 'U.S. States Game',
        'screen_width': 725,
        'screen_height': 491,
    }

    def __init__(self, params=None):
        if not isinstance(params, dict):
            params = {}
        self.params = self.DEFAULT_PARAMS | params

        self.guessed_states = []

        self.screen = turtle.Screen()
        self._prepare_screen_appearance()
        self._prepare_screen_events()

        self.states_explorer = StatesExplorer()
        self.message_writer = MessageWriter()

        turtle.mainloop()

    def _prepare_screen_appearance(self):
        self.screen.setup(width=self.params['screen_width'], height=self.params['screen_height'])
        self.screen.title(self.params['screen_title'])
        self.screen.bgpic('./day25_files/images/map.gif')

    def _prepare_screen_events(self):
        self.screen.listen()
        self.screen.onscreenclick(self._screen_click_processing)

    def _screen_click_processing(self, x, y):
        guessed_states_count = len(self.guessed_states)
        total_states_count = self.states_explorer.get_states_count()

        state_name = self.screen.textinput(
            f'({guessed_states_count}/{total_states_count}) Try to guess!',
            'What state is it?'
        ).title()

        if state_name in ('Exit', 'Quit'):
            self.states_explorer.save_missing_states_to_file(
                self.guessed_states,
                './day25_files/output/missing_states.csv'
            )
            turtle.bye()

        guessed_state = self.states_explorer.find_state(state_name)
        if guessed_state is None:
            return

        delta = self.params['coordinates_delta']

        if guessed_state['x'] - delta < x < guessed_state['x'] + delta \
                and guessed_state['y'] - delta < y < guessed_state['y'] + delta:
            found_state_name = guessed_state['state'].title()
            self.message_writer.goto(guessed_state['x'], guessed_state['y'])
            self.message_writer.write_message(found_state_name)
            self.guessed_states.append(found_state_name)
