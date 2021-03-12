s = input()
t = input()
total = 0
#print(s.startswith.__doc__)

while True:
    if s.startswith(t, s.find(t)):
        total += 1
        s = s[s.find(t) + 1:]
    else:
        print(total)
        break

"""
    if s.startswith(t):
        s = s[1:]
        total += 1
    else:
        print(total)
        break

"""

