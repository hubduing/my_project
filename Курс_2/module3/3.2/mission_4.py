import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"\\", line):
        print(line)