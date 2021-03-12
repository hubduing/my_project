n = int(input())
lst = []
total = 0


for i in range(1, n + 1):
    lst.append(str(i) * i)

for elem in lst:
    if len(elem) < 10:
        for z in elem:
            if total != n:
                total += 1
                print(z, end=" ")
            else:
                break
    else:
        for x in range(0, len(elem), 2):
            if total != n:
                total += 1
                print(elem[x:x + 2], end=" ")
            else:
                break
