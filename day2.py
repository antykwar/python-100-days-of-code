def my_input(hint, separator=' '):
    return input(hint + separator)


print('Welcome to the tip calculator')
total_bill = float(my_input('What was the total bill?', ' $'))
tip_percent = int(my_input('What percentage tip would you like to give (10, 12 or 15)?'))
people_amount = int(my_input('How many people to split the bill?'))

total_sum = total_bill * (1 + tip_percent / 100)
person_sum = round(total_sum / people_amount, 2)

formatted_sum = '{:.2f}'.format(person_sum)

print(f'Each person should pay: ${formatted_sum}')
