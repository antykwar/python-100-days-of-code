def difficulty(value: str):
    available_values = ('easy', 'hard')
    if value.lower() not in available_values:
        raise Exception(f'Difficulty level should be in list: {available_values}')
