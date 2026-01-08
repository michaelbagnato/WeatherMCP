from fastmcp import FastMCP

from models.currentTemp import Temperature
from models.weatherResponse import Weather

from services.wttr import downloadForecast

mcp = FastMCP("Weather")

@mcp.tool
def getCurrentTemperature(city) -> Temperature:
   data = downloadForecast(city)
   return Temperature(temperatureC = int(data.current_condition[0].temp_C))

@mcp.tool
def getForecast(city, daysAhead = 3) -> list[Weather]:
   data = downloadForecast(city)
   return data.weather[:daysAhead]

mcp.run(transport = "http", port=9000)

