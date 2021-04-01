import json
import requests
from flask import request

city = input("Please enter city name : ")
#link = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=1cce1d3fdcf9b8e3576065bd845b8f4d"
#link2 = link.format(city)

data = requests.get("http://api.openweathermap.org/data/2.5/weather?q=patna&appid=1cce1d3fdcf9b8e3576065bd845b8f4d")
#   api = json.loads(data.content)
y = data['main']
current_temprature = y['temp']
humidity = y['humidity']
tempmin = y['temp_min']
tempmax = y['temp_max']

# Coordinates
x = data['coord']
longtitude = x['lon']
latitude = x['lat']

# Country
z = data['sys']
country = z['country']
citi = data['name']

print("Weather of ", city)
print("Temperature", current_temprature)
print("Temp min", tempmin)
print("Temp max", tempmax)
