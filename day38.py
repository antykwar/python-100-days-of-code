import datetime
import os
from pathlib import Path

import requests
from dotenv import load_dotenv


class Nutrition:
    def __init__(self):
        self._app_id = os.environ.get('NUTRITION_APP_ID')
        self._app_key = os.environ.get('NUTRITION_APP_KEY')
        self._endpoint = os.environ.get('NUTRITION_ENDPOINT')

    def _perform_nutrition_request(self, url: str, params: dict):
        headers = {
            'x-app-id': self._app_id,
            'x-app-key': self._app_key,
        }
        response = requests.post(url=url, json=params, headers=headers)
        response.raise_for_status()
        return response

    def get_exercises_data(self, query: str):
        endpoint = f'{self._endpoint}/natural/exercise'
        params = {
            'query': query,
        }
        exercises_data = self._perform_nutrition_request(endpoint, params).json()
        output_data = [{
            'exercise': exercise['name'].capitalize(),
            'duration': int(exercise['duration_min']) if 'duration_min' in exercise else None,
            'calories': int(exercise['nf_calories']) if 'nf_calories' in exercise else None,
        } for exercise in exercises_data['exercises']]
        return output_data


class Sheety:
    def __init__(self):
        self._endpoint = os.environ.get('SHEETY_ENDPOINT')
        self._wrapper = os.environ.get('SHEETY_WRAPPER')
        self._token = os.environ.get('SHEETY_TOKEN')

    def _perform_sheety_request(self, url: str, params: dict):
        headers = {
            'Authorization': f'Bearer {self._token}'
        }
        response = requests.post(url=url, json=params, headers=headers)
        print(response.json())
        response.raise_for_status()
        return response

    def set_exercise_data(self, data: dict):
        current_date = datetime.datetime.now()
        params = {
            self._wrapper: {
                'date': current_date.strftime('%d/%m/%Y'),
                'time': current_date.strftime('%H:%M:%S'),
                'exercise': data['exercise'],
                'duration': int(data['duration']),
                'calories': data['calories'],
            },
        }
        try:
            self._perform_sheety_request(self._endpoint, params)
            return True
        except requests.exceptions.HTTPError:
            return False


if __name__ == '__main__':
    dotenv_path = Path('day38_files/.env')
    load_dotenv(dotenv_path=dotenv_path)

    query = input('Describe your activity, please: ')

    nutrition = Nutrition()
    exercise_descriptions = nutrition.get_exercises_data(query)

    sheety = Sheety()
    for exercise_description in exercise_descriptions:
        sheety.set_exercise_data(exercise_description)

    print('Activities logged')
