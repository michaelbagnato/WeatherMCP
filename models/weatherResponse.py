from dataclasses import dataclass

@dataclass
class Condition:
   temp_C: str

@dataclass
class WeatherResponse:
   current_condition: list[Condition]

