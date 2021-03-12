import requests
'''
r = requests.get("http://example.com")
print(r.text)
'''

url = "https://www.google.ru/"
par = {"par1": "Value1", "par2": "Value2"}

r = requests.get(url, params=par)
print(r.url)

#Как передавать куки
url = "http://httpbin.org/cookies"
cookies = {"cookies_are": "working"}
r = requests.get(url, cookies=cookies)
print(r.text)
print()

print(r.cookies["example_cookies_name"])