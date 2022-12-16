import os
from pathlib import Path
from dotenv import load_dotenv

import requests
import datetime
from datetime import timezone

from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


class RainAlertConfig:
    @staticmethod
    def get_api_key():
        return os.environ['OPENWEATHER_API_KEY']

    @staticmethod
    def get_city():
        return os.environ['OPENWEATHER_HOME_CITY']


class TwillioSmsSenderConfig:
    @staticmethod
    def get_account_sid():
        return os.environ['TWILLIO_ACCOUNT_SID']

    @staticmethod
    def get_auth_token():
        return os.environ['TWILLIO_AUTH_TOKEN']

    @staticmethod
    def get_sender_number():
        return os.environ['TWILLIO_SENDER_NUMBER']

    @staticmethod
    def get_test_receiver_number():
        return os.environ['TWILLIO_TEST_NUMBER']


class TwilioSmsSender:
    def __init__(self, config: TwillioSmsSenderConfig):
        self.config = config

    def send_message(self, text):
        proxy_client = None
        if 'https_proxy' in os.environ:
            proxy_client = TwilioHttpClient()
            proxy_client.session.proxies = {'https': os.environ['https_proxy']}

        client = Client(
            self.config.get_account_sid(),
            self.config.get_auth_token(),
            http_client=proxy_client
        )
        message = client.messages.create(
            from_=self.config.get_sender_number(),
            to=self.config.get_test_receiver_number(),
            body=text
        )
        return message.status == 'queued'


class RainAlert:
    def __init__(self, config: RainAlertConfig):
        self.api_key = config.get_api_key()
        self.city = config.get_city()

    def _perform_request(self, api_url: str, params: dict):
        params['appid'] = self.api_key
        response = requests.get(url=api_url, params=params)
        response.raise_for_status()
        return response

    def _get_city_coords(self):
        response = self._perform_request(
            'https://api.openweathermap.org/data/2.5/weather',
            {'q': self.city}
        )
        return response.json()['coord']

    def _get_forecast(self):
        coords = self._get_city_coords()
        response = self._perform_request(
            'https://api.openweathermap.org/data/2.5/forecast',
            {'lat': coords['lat'], 'lon': coords['lon']}
        )
        return response.json()

    def need_to_take_umbrella(self, hours: int = 12):
        forecast = self._get_forecast()
        current_datetime = datetime.datetime.now(tz=timezone.utc).replace(tzinfo=timezone.utc)
        finish_timestamp = current_datetime.timestamp() + hours * 3600
        for data_block in forecast['list']:
            if data_block['dt'] > finish_timestamp:
                break
            weather = data_block['weather'].pop()
            if weather['id'] < 700:
                return True
        return False


if __name__ == '__main__':
    dotenv_path = Path('day35_files/.env')
    load_dotenv(dotenv_path=dotenv_path)

    if RainAlert(RainAlertConfig()).need_to_take_umbrella(12):
        TwilioSmsSender(TwillioSmsSenderConfig()).send_message('Hey, you will need an umbrella today!')
