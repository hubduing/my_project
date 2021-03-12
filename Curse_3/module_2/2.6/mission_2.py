res = []
total = 0
n = int(input())
if n == 0:
    print(0)
for i in range(1, n + 1):
    res.extend(str(i) * i)
#print(*res)
for j in res:
    if total != n:
        total += 1
        print(j, end=" ")
    else:
        break