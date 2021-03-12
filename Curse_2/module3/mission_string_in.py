s = input()
a = input()
b = input()
total = 0
for i in range(1001):
    if a in s:
        s = s.replace(a, b)
        total += 1
    else:
        print(total)
        break
else:
    print('Impossible')