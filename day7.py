from random import choice

from day7_modules.art import *
from day7_modules.words import *


def get_blanks(word):
    return ['_'] * len(word)


def fill_blanks(blanks, letters_map, letter):
    return list(map(lambda symbol, map_value: letter if map_value else symbol, blanks, letters_map))


def has_blanks(blanks):
    return '_' in blanks


def print_blanks(blanks):
    print(' '.join(blanks))


def has_matches(matching_map):
    return matching_map.count(True) > 0


def letter_map_factory(word):
    def letter_map_factory_result(letter):
        return [current_letter == letter for current_letter in word]
    return letter_map_factory_result


def get_current_stage():
    return stages.pop()


def has_more_stages():
    return len(stages) > 0


word_to_guess = choice(word_list)
print(logo)

blanks = get_blanks(word_to_guess)
guessed_letters = set()
letter_map = letter_map_factory(word_to_guess)
current_stage = False

while True:
    input_letter = input("Please input a letter:\n").lower()

    if input_letter in guessed_letters:
        print(f'You already tried this letter: {input_letter}')
        continue

    guessed_letters.add(input_letter)

    matching_map = letter_map(input_letter)
    blanks = fill_blanks(blanks, matching_map, input_letter)

    print_blanks(blanks)

    if not has_blanks(blanks):
        print('You win!')
        break

    if has_matches(matching_map):
        if current_stage:
            print(current_stage)
        continue
    else:
        current_stage = get_current_stage()
        if not current_stage:
            current_stage = get_current_stage()
        print(current_stage)
        print(f'You tried \'{input_letter}\', but it is not in the word :(')
        if not has_more_stages():
            print(f'You loose... The word was: {word_to_guess}')
            break
