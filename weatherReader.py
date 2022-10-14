
import time
import pyttsx3
import requests
import time

# Setting up the engine for speech
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 10)

volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.60)

sound = engine.getProperty ('voices');
engine.setProperty('voice', 'sound[1].id')


engine.say("Which city Sir?")
engine.runAndWait()
api_key = "6f06ee7a096d9b0b7d5b3c5bda07c46e"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input("Please enter the city name you want to get information about:").title()
print(str(city_name)+" Weather report:\n")
complete_url = base_url + "appid=" + api_key + \
    "&q=" + city_name + "&units=metric"

response = requests.get(complete_url)
x = response.json()
# print(x)
if x["cod"] != "404":

    y = x["main"]
    current_temperature = y["temp"]

    current_pressure = y["pressure"]
    current_city = x["name"]
    current_humidiy = y["humidity"]

    z = x["weather"]

    weather_description = z[0]["description"]

    print(" Temperature (kelvin) = " +
            str(current_temperature) +
            "\n atmospheric pressure (hPa) = " +
            str(current_pressure) +
            "\n humidity () = " +
            str(current_humidiy) + "%" +
            "\n description = " +
            str(weather_description))
    engine.say(str(current_city)+" Temperature (in celcius unit) = " +
            str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
            str(current_pressure) +
            "\n humidity (in percentage) = " +
            str(current_humidiy) +
            "\n description = " +
            str(weather_description))
    engine.runAndWait()

else:
    print(" City Not Found ")