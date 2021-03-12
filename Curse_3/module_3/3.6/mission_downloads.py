import requests

with open("dataset_3378_2.txt") as f, open("result", "w") as res:
    url = f.readline().strip()
    r = requests.get(url)
    number = r.text.splitlines()
    res.write(str(len(number)))