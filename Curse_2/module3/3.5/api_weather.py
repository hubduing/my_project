# key=b2aa9137771fc6187fd285b4eb1aff1f
import requests

city = input("City? ")

api_url = "http://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": "b2aa9137771fc6187fd285b4eb1aff1f",
    "units": "metric"
}

res = requests.get(api_url, params=params)
#print(res.status_code)
#print(res.headers["Content-Type"])
#print(res.json()) #return json loads(res.text)
data = res.json() # словарь
teplate = "Current temperature in {} is {}"

print(teplate.format(city, data["main"]["temp"]))