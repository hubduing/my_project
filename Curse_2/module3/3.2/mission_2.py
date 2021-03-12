import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(r"\bcat\b", line):
        print(line)