import requests

res = requests.get("https://www.google.com/webhp?hl=ru&sa=X&ved=0ahUKEwid_tm-lK_uAhVbCRAIHUWkDeYQPAgI",
                   params={
                       "text": "Stepic",
                       "test": "test1",
                       "name": "No_Name",
                       "list": ["tast1", "test2"]
                   })
print(res.status_code)
print(res.headers["Content-Type"])

print(res.url)
#print(res.text)

#with open("python.png", "wb") as f:
#    f.write(res.content)
