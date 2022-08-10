import random
import string


letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password_elements = random.choices(letters, k=nr_letters) \
                  + random.choices(numbers, k=nr_numbers) \
                  + random.choices(symbols, k=nr_symbols)

random.shuffle(password_elements)
print(''.join(password_elements))
