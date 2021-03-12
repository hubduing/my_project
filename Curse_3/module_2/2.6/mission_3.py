n = int(input())
total = 1
lst = [i for i in range(1, n ** 2 + 1)]
for i in range(1, len(lst)):
    if i == n + 1:
        print()
        break
    else:
        print(i, end=" ")
for x in range(n + 1, len(lst) + 1):
    if total == n + 2:
        total = 1
        print()
    else:
        total += 1
        print(x, end=" ")
