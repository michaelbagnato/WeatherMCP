from dacite import from_dict
from json import loads
from urllib.request import urlopen

from models.weatherResponse import WeatherResponse

def downloadForecast(city: str) -> WeatherResponse:
   weather_data = loads(urlopen(f"http://wttr.in/{city}?format=j1").read())
   weatherResponse = from_dict(data_class=WeatherResponse, data=weather_data) 
   return weatherResponse
