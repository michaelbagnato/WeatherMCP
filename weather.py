from fastmcp import FastMCP

from models.currentTemp import Temperature
from services.wttr import downloadForecast

mcp = FastMCP("Weather")

@mcp.tool
def getCurrentTemperature(city) -> Temperature:
   data = downloadForecast(city)
   return Temperature(temperatureC = int(data.current_condition[0].temp_C))

mcp.run(transport = "http", port=9000)

