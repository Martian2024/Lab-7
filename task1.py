import requests 
import os
import json

CITY_NAME = 'St. Petersburg'
API_KEY = os.environ['APIKEY']

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric')
if response.ok:
    print(f"""Current weather in {response.json()['name']}:

Weather: {response.json()['weather'][0]['description']}
Temperature, C: {response.json()['main']['temp']}
Pressure, hPa: {response.json()['main']['pressure']}
Humidity, %: {response.json()['main']['humidity']}""")
else:
    print('Something went terribly wrong...')



