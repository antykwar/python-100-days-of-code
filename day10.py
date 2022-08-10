from day10_modules import art


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError('Can not divide by zero')
    return a / b


operations = {
    '+': add,
    '-': sub,
    '*': multiply,
    '/': divide,
}

print(art.logo)
print("Available operations:\n" + "\n".join(operations.keys()) + "\n")
last_result = None

while True:
    if last_result is None:
        num1 = float(input('First number? '))
    else:
        num1 = last_result
    operation = input('Operation? ')
    num2 = float(input('Next number? '))

    try:
        last_result = operations[operation](num1, num2)
        print(f'{num1} {operation} {num2} = {last_result}')
    except ValueError as error:
        print('Error: ' + str(error))

    next_action = input(f'Use {last_result}? Or type \'x\' to exit.').lower()
    if next_action == 'x':
        break

    use_last_result = (next_action == 'y')
    if last_result is not None and use_last_result:
        continue
    last_result = None
