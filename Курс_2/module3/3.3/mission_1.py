import requests
import re

def requesty(ha):
    _ = requests.get(ha)
    if re.findall(r'href=[\'\"]?([^\'\" >]+)', _.text) == href2:
        print("YES")
    else:
        print("NO")


#href = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
href = str(input())
#href2 = "https://stepic.org/media/attachments/lesson/24472/sample2.html"
href2 = str(input())
res_a = requests.get(href)
if re.findall(r'href=[\'\"]?([^\'\" >]+)', res_a.text):
    #print(a.group(1))
    _ = re.findall(r'href=[\'\"]?([^\'\" >]+)', res_a.text)
    requesty(_)

# пример
# b'<a href="https://stepic.org/media/attachments/lesson/24472/sample1.html">1</a>\n'