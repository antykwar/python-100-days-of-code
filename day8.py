from pyinputplus import inputCustom, inputYesNo

from day8_modules.art import logo


def get_transform_list(shift, decrypt=False):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
               'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']

    encode_list = {
        letters[key]: letters[key + shift if key + shift < len(letters) else (key + shift) % len(letters)]
        for key, value in enumerate(letters)
    }

    return {v: k for k, v in encode_list.items()} if decrypt else encode_list


def caesar(text, shift, direction):
    dictionary = get_transform_list(shift, decrypt=(direction == 'decode'))
    string = ''
    for symbol in text:
        string += dictionary[symbol] if symbol in dictionary else symbol
    return string


def validate_direction(direction):
    allowed_values = ('encode', 'decode', 'exit')
    if direction not in allowed_values:
        raise Exception("Please enter 'encode' or 'decode' (or 'exit' to, actually, exit):")


def validate_shift(shift):
    if not shift.isdigit() or shift.startswith('0'):
        raise Exception("Please enter positive integer number:")
    return int(shift)


print(logo)

while True:
    direction = inputCustom(validate_direction, prompt='What should we do now (encode, decode, exit)?: ')

    if direction == 'exit':
        print('Goodbye, My Caesar!')
        break

    text = input("Type your message:\n").lower()

    shift = inputCustom(validate_shift, prompt='Type the shift number: ')

    print(f'The {direction}d result is: ' + caesar(text, shift, direction))

    a = inputYesNo('Do you want to proceed?:')

    if a != 'yes':
        print('Goodbye, My Caesar!')
        break
