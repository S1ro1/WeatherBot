from datetime import datetime
import requests
from convert_to_chart import convert

url = "https://api.openweathermap.org/data/2.5/onecall?lat="
url2 = "https://api.openweathermap.org/data/2.5/forecast?lat="

def get_5day_weather(coordinates, key):
    request_url = f"{url2}{coordinates[0]}&lon={coordinates[1]}&units=metric&appid={key}"
    data = requests.get(request_url).json()["list"]

    for index, value in enumerate(data):
        day = datetime.fromtimestamp(data[index]["dt"]).date().strftime('%A')
        time = datetime.fromtimestamp(data[index]["dt"]).time()
        temp = round(data[index]["main"]["temp"], 1)
        description = data[index]["weather"][0]["description"]

        data[index] = [day, time, temp, description]

    return convert(data, 0)

def get_current_weather(coordinates, key):
    exclude = "minutely,hourly,daily,alerts"
    request_url = f"{url}{coordinates[0]}&lon={coordinates[1]}&units=metric&exclude={exclude}&appid={key}"
    data = requests.get(request_url).json()["current"]

    time = datetime.fromtimestamp(data["dt"]).time()

    data = [[time, data["temp"], data["wind_speed"], data["weather"][0]["description"]]]

    return convert(data, 1)

def get_48h_weather(coordinates, key):
    exclude = "current,minutely,daily,alerts"
    request_url = f"{url}{coordinates[0]}&lon={coordinates[1]}&units=metric&exclude={exclude}&appid={key}"
    data = requests.get(request_url).json()["hourly"]

    for index, value in enumerate(data):
        time = datetime.fromtimestamp(value["dt"]).time()
        temp = value["temp"]
        description = value["weather"][0]["description"]
        data[index] = [time, temp, description]

    return convert(data, 2)

def get_7day_weather(coordinates, key):
    exclude = "current,minutely,hourly,alerts"
    request_url = f"{url}{coordinates[0]}&lon={coordinates[1]}&units=metric&exclude={exclude}&appid={key}"
    data = requests.get(request_url).json()["daily"]

    for index, value in enumerate(data):
        time = datetime.fromtimestamp(value["dt"]).date()
        temp = value["temp"]
        description = value["weather"][0]["description"]

        data[index] = [time, temp["morn"], temp["day"], temp["eve"], temp["night"], description]

    return convert(data, 3)
