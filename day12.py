from random import randint
from pyinputplus import inputCustom, inputInt

from day12_modules.validation import difficulty


ATTEMPTS_EASY = 10
ATTEMPTS_HARD = 5

difficulty = inputCustom(difficulty, prompt='Please select game difficulty (easy, hard)?: ')
number_to_guess = randint(1, 100)
attempts_number = ATTEMPTS_EASY if difficulty == 'easy' else ATTEMPTS_HARD
is_success = False

while attempts_number > 0:
    print(f'You have {attempts_number} chance(s) to guess')
    guess = inputInt(prompt='Try to guess\n', min=1, max=100)
    attempts_number -= 1

    if guess == number_to_guess:
        is_success = True
        break

    print('Too low!' if guess < number_to_guess else 'Too high!')

success_status = 'win' if is_success else 'lost'
print(f'You {success_status}, guessed number was {number_to_guess}.')
