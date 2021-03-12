import sys
import re
for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\ba+\b"
    line = re.sub(pattern, "argh", line, count=1, flags=re.IGNORECASE)
    print(line)