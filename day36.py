import os
import requests
import datetime
import itertools

from pytz import timezone
from enum import Enum
from pathlib import Path
from dotenv import load_dotenv


class StockCode(Enum):
    TESLA = 'TSLA'


class CompanyName(Enum):
    TESLA = 'Tesla Inc'


class MarketDataExplorer:
    def __init__(self, stock_code=None):
        self._api_url = os.environ.get('MARKET_API_URL')
        self._api_key = os.environ.get('MARKET_API_KEY')
        self.stock_code = stock_code

    def _perform_request(self, params: dict):
        params['apikey'] = self._api_key
        response = requests.get(url=self._api_url, params=params)
        response.raise_for_status()
        return response

    def _get_time_series_daily_adjusted(self):
        params = {
            'function': 'TIME_SERIES_DAILY_ADJUSTED',
            'symbol': self.stock_code,
        }
        series = self._perform_request(params)
        return series.json()['Time Series (Daily)']

    def get_price_diff_percent(self):
        tz = timezone('EST')
        yesterday_date = datetime.datetime.now(tz) - datetime.timedelta(days=1)
        last_key = yesterday_date.strftime('%Y-%m-%d')

        series = self._get_time_series_daily_adjusted()
        if last_key not in series:
            return None

        series = list(dict(itertools.islice(series.items(), 2)).values())
        diff_percent = ((float(series[1]['4. close']) - float(series[0]['4. close']))
                        / float(series[1]['4. close'])) * 100
        return diff_percent


class NewsExplorer:
    def __init__(self, company_name=None):
        self._api_url = os.environ.get('NEWS_API_URL')
        self._api_key = os.environ.get('NEWS_API_KEY')
        self.company_name = company_name

    def _perform_request(self, params: dict):
        params['apiKey'] = self._api_key
        response = requests.get(url=self._api_url, params=params)
        response.raise_for_status()
        return response

    def _get_last_news(self, count):
        params = {
            'pageSize': count,
            'q': self.company_name
        }
        news_response = self._perform_request(params)
        return news_response.json()['articles']

    def get_news(self, count=3):
        news_data = self._get_last_news(count)
        return [{
            'title': piece_of_news['title'],
            'description': piece_of_news['description']
        } for piece_of_news in news_data]


class MessageSender:
    @staticmethod
    def send_message(message):
        print(message)


if __name__ == '__main__':
    dotenv_path = Path('day36_files/.env')
    load_dotenv(dotenv_path=dotenv_path)

    market_explorer = MarketDataExplorer(StockCode.TESLA.value)
    current_price_diff_percent = market_explorer.get_price_diff_percent()

    sign = StockCode.TESLA.value + ': ' + ('🔺' if current_price_diff_percent > 0 else '🔻')
    current_price_diff_percent_show = sign + '{:.2f}%'.format(abs(current_price_diff_percent))

    if abs(current_price_diff_percent) > 1:
        news_explorer = NewsExplorer(CompanyName.TESLA.value)
        news = news_explorer.get_news()
        for article in news:
            current_price_diff_percent_show += f"\nHeadline: {article['title']}\nBrief: {article['description']}"
        MessageSender.send_message(current_price_diff_percent_show)
