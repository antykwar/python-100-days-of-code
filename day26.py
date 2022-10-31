import pandas

dictionary_data = pandas.read_csv('day26_files/nato_phonetic_alphabet.csv')
nato_dictionary = {row.letter: row.code for (key, row) in dictionary_data.iterrows()}

while True:
    input_word = input("Word:\n")
    try:
        print([nato_dictionary[word.upper()] for word in input_word])
        break
    except KeyError:
        print('Sorry, only English alphabet.')

