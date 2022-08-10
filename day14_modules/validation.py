def variants(value: str):
    available_values = ('A', 'B')
    if value.upper() not in available_values:
        raise Exception(f'Please choose from list: {available_values}')
