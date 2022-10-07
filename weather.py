key= 'ab5bf4b0970860437fc442604639d812' # for openweathermap
import json
import urllib.request

def weather(city):
  url =f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}' #url to read brampton weather data, where city = brampton 
  response = urllib.request.urlopen(url) #fetching url
  result = json.loads(response.read())
  print(result)