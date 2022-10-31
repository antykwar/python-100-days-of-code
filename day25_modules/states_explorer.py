import pandas


class StatesExplorer:
    def __init__(self):
        self.states = pandas.read_csv('./day25_files/data/states.csv')
        self.states_count = len(self.states)

    def find_state(self, state_name: str):
        if not state_name:
            return None
        state = self.states[self.states.state == state_name.strip()]
        if state.empty:
            return None
        state_data = state.to_dict(orient='records')
        return state_data[0]

    def _find_missing_states(self, guessed_states: list):
        return self.states[~self.states.state.isin(guessed_states)]

    def save_missing_states_to_file(self, guessed_states, filename):
        missing_states = self._find_missing_states(guessed_states)
        missing_states.to_csv(filename)

    def get_states_count(self):
        return self.states_count
