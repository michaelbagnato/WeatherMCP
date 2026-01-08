from fastmcp import FastMCP
from json import loads
from urllib.request import urlopen

mcp = FastMCP("Weather")

@mcp.tool
def getWeather(city):
   response = urlopen(f"http://wttr.in/{city}?format=j2").read()
   weatherData = loads(response)
   return { "temperatureC": weatherData["current_condition"][0]["temp_C"] }

mcp.run(transport = "http", port=9000)

