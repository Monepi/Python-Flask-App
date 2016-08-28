import requests


def get_weather(city, days):
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?id="+city+"&units=metric&cnt="+days+"&appid=466a2d0c5a6d7a56d27c16bfc95ae658"
    response = requests.get(url)
    return response.json()


