import re
import requests
from urllib.parse import urlparse



#https://pastebin.com/raw/7543p0ns
lst = []
result = []
url_input = requests.get(input()).text
#print(url_input)
#pattern = r"href=[\'\"]?http:\/\/([^\'\" \/]+)"
#pattern = r"href=[\'\"]?http:\/\/([^\'\" \/?\:?]+)"
pattern = r"<a.*?href=(?:[\'|\"][\w://]+://)([\w.-]+)(?:[\/:\'\"])>?"

lst.extend(re.findall(pattern, url_input))

lst = set(lst)
lst = list(lst)
lst.sort()
#for i in lst:
#    if requests.get(i):
#        result.append(i)
print(*lst, sep="\n")
#print(*result, sep="\n")