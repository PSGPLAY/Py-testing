api = "94ce99aab897d2c54034495bbeaa75fe"

import requests

input_city = input("Enter city name: ")
r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={input_city}&appid=" + api, stream=True)

data = r.json()
# print(data)


try:
   print("The sky is", data["weather"][0]["main"], ", the Humidity is", data["main"]["humidity"], "and the temperature is", round(data["main"]["temp"] - 273.15, 2), "°C with the wind speed of", data["wind"]["speed"], "m/s")

except KeyError:
   print("City not found!")