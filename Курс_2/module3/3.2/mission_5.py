import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"\b(\w+)\1\b", line):
        print(line)
