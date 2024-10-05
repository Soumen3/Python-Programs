import requests
from datetime import datetime
# import json

apiKey = 'ce1be01765cc4d9a824d4fd9986e68b2'
cityName = input("Enter your city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"
print(url)

response = requests.get(url)
data = response.json()
print(data)

kelvinTemp = data['main']['temp']
celsiusTemp = kelvinTemp-273.15
fahrenheitTemp = (celsiusTemp * 9)/5 + 32
feels_like=data['main']['feels_like']-273.15
humidity=data["main"]["humidity"]
windSpeed=data["wind"]["speed"]
clouds=data["clouds"]["all"]
pressure=data["main"]["pressure"]
countryCode=data["sys"]["country"]
sunriseTime=datetime.fromtimestamp((int)(data["sys"]["sunrise"])).strftime('%H:%M')
sunsetTime=datetime.fromtimestamp((int)(data["sys"]["sunset"])).strftime('%H:%M')

timezone=(float)((int)(data["timezone"]))/(60*60)



print(f"current temparature fahrenheit: {fahrenheitTemp:.2f}")
print(f"current temparature celcius: {celsiusTemp:.2f}")

cloudiness = data["clouds"]["all"]
print(f"Cloudiness: {cloudiness}%")
