from datetime import datetime
import requests
from convert_to_chart import convert

url = "https://api.openweathermap.org/data/2.5/onecall?lat="
url2 = "https://api.openweathermap.org/data/2.5/forecast?lat="

def get_5day_weather(coordinates, key):
    request_url = f"{url2}{coordinates[0]}&lon={coordinates[1]}&units=metric&appid={key}"
    data = requests.get(request_url).json()["list"]

    for index, value in enumerate(data):
        day = datetime.fromtimestamp(data[index]["dt"]).strftime("%d/%m:%H:%M")
        temp = round(data[index]["main"]["temp"], 1)
        description = data[index]["weather"][0]["description"]

        data[index] = [day, temp, description]

    return convert(data, 0)

def get_current_weather(coordinates, key):
    exclude = "minutely,hourly,daily,alerts"
    request_url = f"{url}{coordinates[0]}&lon={coordinates[1]}&units=metric&exclude={exclude}&appid={key}"
    data = requests.get(request_url).json()["current"]

    temp = round(data["temp"], 1)
    time = datetime.fromtimestamp(data["dt"]).strftime("%H:%M:%S")
    wind = data["wind_speed"]
    description = data["weather"][0]["description"]

    data = [[time, temp, wind, description]]

    return convert(data, 1)

def get_48h_weather(coordinates, key):
    exclude = "current,minutely,daily,alerts"
    request_url = f"{url}{coordinates[0]}&lon={coordinates[1]}&units=metric&exclude={exclude}&appid={key}"
    data = requests.get(request_url).json()["hourly"]

    for index, value in enumerate(data):
        time = datetime.fromtimestamp(value["dt"]).strftime("%H:%M")
        temp = round(value["temp"],1 )
        description = value["weather"][0]["description"]

        data[index] = [time, temp, description]

    return convert(data, 2)

def get_7day_weather(coordinates, key):
    exclude = "current,minutely,hourly,alerts"
    request_url = f"{url}{coordinates[0]}&lon={coordinates[1]}&units=metric&exclude={exclude}&appid={key}"
    data = requests.get(request_url).json()["daily"]

    for index, value in enumerate(data):
        time = datetime.fromtimestamp(value["dt"]).strftime("%D")
        temp = value["temp"]
        description = value["weather"][0]["description"]

        data[index] = [time, round(temp["morn"], 1), round(temp["day"], 1), round(temp["eve"], 1), round(temp["night"], 1), description]

    return convert(data, 3)
