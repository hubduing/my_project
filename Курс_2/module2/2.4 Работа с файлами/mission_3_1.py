import os
import os.path
lst = []
with open("path.txt", 'w') as path:
    os.chdir("C:/main")
    for current_dir, dirs, files in os.walk(""):
        for file in files:
            if file[-3:] == '.py':
                lst.append(current_dir)
                temp = set(lst)
                lst = list(temp)
                lst.sort()
    for i in lst:
        path.write(i[2:] + '\n')
    path.close()
