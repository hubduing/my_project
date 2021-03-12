'''
Брал первую ссылку, читал с нее все урлы через findall. В скобки взял только урл.

Далее обычным for проходимся по списку урлов, опять все ссылки записываем в новый список методом extend.

В конце обычная проверка наличия второй ссылки во втором списке через in. Если есть - отлично, нет - No.
'''


import requests
import re

href = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
#href = str(input())
href2 = "https://stepic.org/media/attachments/lesson/24472/sample2.html"
#href2 = str(input())
#получил ссылки
lin = requests.get(href)
lin2 = requests.get(href2)
#создал список из ссылок
lst = []
lst.extend(re.findall(r'href=[\'\"]?([^\'\" >]+)', lin.text))
#print(lst)
lst2 = [] # создал список 2
for i in lst:
    a = requests.get(i) # перехожу по 1 ссыле
    lst2.extend(re.findall(r'href=[\'\"]?([^\'\" >]+)', a.text))
    #print(lst2)
# если 2 ссылка есть в 2 списке
if href2 in lst2:
    print("YES")
else:
    print("NO")

