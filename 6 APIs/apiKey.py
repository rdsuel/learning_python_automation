# How to use an API key.  Most APIs require a key so they can track your usage.
import requests

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': '<Your Key Here>', 'q': 'Seattle, US'}
response = requests.get(baseUrl, params=parameters)
print(response.text)