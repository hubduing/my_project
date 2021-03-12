import sys
import re
for line in sys.stdin:
    line = line.rstrip()

    pattern = r"\b(\w)(\w)"
    line = re.sub(pattern, r"\2\1", count=1, flags=re.IGNORECASE)
    print(line)