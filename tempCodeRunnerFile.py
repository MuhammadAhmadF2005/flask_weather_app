import requests
from dotenv import load_dotenv
from dataclasses import dataclass
import os

load_dotenv()
api_key = os.getenv('API_KEY')  # gets api key from .env file !!!

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float

def get_lat_lon(city_name, state_code, country_code, api_key):
    response = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={api_key}'
    ).json()
    
    if response:  # Check if the list is not empty
        data = response[0]
        lat, lon = data.get('lat'), data.get('lon')
        return lat, lon
    else:
        print("No location data found.")
        return None, None

def get_current_weather(lat, lon, api_key):
    if lat is not None and lon is not None:
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
        ).json()

        data = WeatherData(
            main=response.get('weather')[0].get('main'),
            description=response.get('weather')[0].get('description'),
            icon=response.get('weather')[0].get('icon'),
            temperature=response.get('main').get('temp')
        )

        return data
    else:
        print("Invalid coordinates.")
        return None

if __name__ == "__main__":
    lat, lon = get_lat_lon('Toronto', 'ON', 'Canada', api_key)
    print(get_current_weather(lat, lon, api_key))
