import requests
import json

with open("dataset_24476_3.txt") as f, open("result.json", "w") as data_result:
    reader = []
    reader = f.read().rstrip()
    #print(reader)
    for row in reader:
        api_url = f'http://numbersapi.com/{row}/math?json'
        params = {
            "type": "math",
            'json': True,
            "default": "Boring"
        }
        res = requests.get(api_url, params=params) #делаю запрос
        data = res.json() #создаю список
        if data["found"] == True:
            print("Interesting")
            #json.dump(Interesting, data_result)
        else:
            print("Boring")
            #json.dump(Boring, data_result)
