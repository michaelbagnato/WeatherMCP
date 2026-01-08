from dataclasses import dataclass

@dataclass
class Condition:
   temp_C: str

@dataclass
class Weather:
   avgtempC: str
   date: str

@dataclass
class WeatherResponse:
   current_condition: list[Condition]
   weather: list[Weather]
