import smtplib
import time

import requests
from datetime import datetime


MY_LATITUDE = 55.145333
MY_LONGITUDE = 61.382199


MY_SMTP = 'my_smtp'
MY_EMAIL = 'my_email'
MY_PASSWORD = 'my_password'


def iss_is_near(latitude: float, longitude: float) -> bool:
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    iss_position = {key: float(value) for key, value in response.json()['iss_position'].items()}
    return abs(iss_position['latitude'] - latitude) <= 5 and abs(iss_position['longitude'] - longitude) <= 5


def is_currently_dark(latitude: float, longitude: float) -> bool:
    request_params = {
        'lat': latitude,
        'long': longitude,
        'formatted': 0,
    }
    response = requests.get(url='http://api.sunrise-sunset.org/json', params=request_params)
    response.raise_for_status()
    sunrise_sunset = {key: value for key, value in response.json()['results'].items() if key in ['sunrise', 'sunset']}
    sunrise = datetime.strptime(sunrise_sunset['sunrise'], '%Y-%m-%dT%H:%M:%S+00:00')
    sunset = datetime.strptime(sunrise_sunset['sunset'], '%Y-%m-%dT%H:%M:%S+00:00')
    return datetime.now() < sunrise or datetime.now() > sunset


if __name__ == '__main__':
    while True:
        if is_currently_dark(MY_LATITUDE, MY_LONGITUDE) and iss_is_near(MY_LATITUDE, MY_LONGITUDE):
            with smtplib.SMTP(MY_SMTP) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f'Subject:Look up!\n\nISS is near!'
                        )
        print('Wait for another minute...')
        time.sleep(60)
