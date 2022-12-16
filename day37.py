import datetime
import os
import random
from pathlib import Path

import requests
from dotenv import load_dotenv


class PixelaTracker:
    def __init__(self):
        self._username = os.environ.get('SERVICE_USERNAME')
        self._token = os.environ.get('TOKEN')
        self._api_endpoint = os.environ.get('API_ENDPOINT')
        self._graph_id = os.environ.get('GRAPH_ID')
        self._graph_name = os.environ.get('GRAPH_NAME')

    def _perform_post_request(self, url: str, params: dict, auth: bool = True):
        headers = {}
        if auth:
            headers['X-USER-TOKEN'] = self._token
        response = requests.post(url=url, json=params, headers=headers)
        response.raise_for_status()
        return response

    def create_user(self):
        params = {
            'token': self._token,
            'username': self._username,
            'agreeTermsOfService': 'yes',
            'notMinor': 'yes',
        }
        try:
            self._perform_post_request(self._api_endpoint, params, auth=False)
            return True
        except requests.exceptions.HTTPError as error:
            return error.response.status_code == 409

    def create_graph(self):
        params = {
            'id': self._graph_id,
            'name': self._graph_name,
            'unit': 'commit', 
            'type': 'int', 
            'color': 'shibafu',
        }
        try:
            endpoint = f'{self._api_endpoint}/{self._username}/graphs'
            self._perform_post_request(endpoint, params)
            return True
        except requests.exceptions.HTTPError as error:
            return error.response.status_code == 409

    def create_record(self, date: str, quantity: int):
        params = {
            'date': str(date),
            'quantity': str(quantity),
        }
        try:
            endpoint = f'{self._api_endpoint}/{self._username}/graphs/{self._graph_id}'
            self._perform_post_request(endpoint, params)
            return True
        except requests.exceptions.HTTPError as error:
            return error.response.status_code == 409


if __name__ == '__main__':
    dotenv_path = Path('day37_files/.env')
    load_dotenv(dotenv_path=dotenv_path)

    pixela_tracker = PixelaTracker()
    if not pixela_tracker.create_user():
        print('Problems while creating/checking user, exiting.')
        exit(1)
    if not pixela_tracker.create_graph():
        print('Problems while creating/checking graph, exiting.')
        exit(2)

    # Here we can get/validate input (date, quantity, graph name, ...), now using sample data
    date = datetime.datetime.now().strftime('%Y%m%d')
    quantity = random.randint(1, 15)

    if not pixela_tracker.create_record(date, quantity):
        print('Problems while creating record, exiting.')
        exit(4)
    print('Record successfully added!')
