import re

for line in input():
    x = re.findall(r"(cat|\.?)", line)
    if x.count('cat') >= 2:
        print(line)

'''
catcat
cat and cat
catac
cat
ccaatt
'''