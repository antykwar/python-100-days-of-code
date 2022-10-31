import pandas as pd
import random


class DataProvider:
    def __init__(self, new_language, known_language):
        self.new_language = new_language
        self.known_language = known_language
        self.current_word_index = None
        self.current_new_word = None
        self.current_known_word = None
        self._current_dictionary = self._load_dictionary(new_language)

    @staticmethod
    def _load_dictionary(new_language):
        try:
            data_frame = pd.read_csv(f'day31_files/output/{new_language.lower()}_words_to_learn.csv')
        except FileNotFoundError:
            data_frame = pd.read_csv(f'day31_files/data/{new_language.lower()}_words.csv')
        finally:
            prepared_dictionary = data_frame.to_dict(orient='index')
            return prepared_dictionary

    def get_random_word(self):
        if len(self._current_dictionary) == 0:
            return None
        word_key = random.choice(list(self._current_dictionary))
        word = self._current_dictionary[word_key]
        self.current_word_index = word_key
        self.current_new_word = word[self.new_language]
        self.current_known_word = word[self.known_language]
        return {'new': self.current_new_word, 'known': self.current_known_word}

    def mark_word_as_known(self, is_word_known):
        if is_word_known is not True:
            return
        self._current_dictionary.pop(self.current_word_index, None)

        new_data_frame = pd.DataFrame.from_dict(self._current_dictionary, orient='index')
        new_data_frame.to_csv(f'day31_files/output/{self.new_language.lower()}_words_to_learn.csv', index=False)
