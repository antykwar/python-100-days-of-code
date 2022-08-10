import random
from cerberus import Validator


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

variants = [rock, paper, scissors]

user_selection_index = input('What do you choose? 0 - Rock, 1 - Paper, 2 - Scissors: ')
validationScheme = {'index': {'type': 'integer', 'min': 0, 'max': 2, 'required': True, 'coerce': int}}
validator = Validator(validationScheme)

if not validator.validate({'index': user_selection_index}):
    print('Wrong number, you looose :(')
    quit()

computer_selection_index = random.randint(0, len(variants) - 1)
user_selection_index = validator.document['index']

print(variants[user_selection_index])
print('Computer chooses:')
print(variants[computer_selection_index])

if computer_selection_index == user_selection_index:
    print('It`s a draw :)')
    quit()

if abs(user_selection_index - computer_selection_index) == 1:
    print('You win!' if user_selection_index > computer_selection_index else 'You loose :(')
    quit()

print('You win!' if (user_selection_index == 0) else 'You loose :(')
