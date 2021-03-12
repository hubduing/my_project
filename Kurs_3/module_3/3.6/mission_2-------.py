import requests

with open("dataset_3378_3.txt") as f:
    url = f.readline()
    for i in range(3):
        r = requests.get(url)
        url = r.url
        print(r.url)