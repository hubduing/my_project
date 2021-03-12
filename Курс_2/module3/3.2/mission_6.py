import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"human"
    if re.sub(pattern, "computer", line):
        print(line)
