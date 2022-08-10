# Debugging
# from random import randint
#
#
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
#
#
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)


# Describe Problem
# my_function()

# Reproduce the Bug
# dice_images = {1: "❶", 2: "❷", 3: "❸", 4: "❹", 5: "❺", 6: "❻"}
# dice_num = randint(1, 6)
# print(dice_images[dice_num])

# Play Computer
# year = int(input("What's your year of birth? "))
# if 1980 < year < 1994:
#     print("You are a millennial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

# Fix the Errors
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")

# Print is Your Friend
# pages = int(input("Number of pages: ")) or 0
# word_per_page = int(input("Number of words per page: ")) or 0
# total_words = pages * word_per_page
# print(total_words)

# Use a Debugger
# mutate([1, 2, 3, 5, 8, 13])

# Even or Odd
# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")
#

# Leap year
# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# FizzBuzz
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
