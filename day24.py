import os

with open('day24_files/input/names/invited_names.txt', mode='r') as names_reader:
    names = [name.rstrip() for name in names_reader.readlines()]

with open('day24_files/input/letters/starting_letter.txt', mode='r') as letter_reader:
    letter = [line.rstrip() for line in letter_reader.readlines()]
letter_text = '\n'.join(letter).rstrip()

for name in names:
    file_name = f"letter_to_{name.replace(' ', '_')}.txt"
    with open('day24_files/output/ready_to_send/' + file_name, mode='w') as letter_writer:
        letter_writer.write(letter_text.replace('[name]', name))


