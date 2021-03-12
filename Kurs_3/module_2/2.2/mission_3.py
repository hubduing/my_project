a, b = int(input()), int(input())
c, d = int(input()), int(input())


for _ in range(c, d + 1):
    if _ == c:
        print(end="\t")
    print(_, end="\t")
print()
for i in range(a, b + 1):
    print(i, end="\t")
    for j in range(c, d + 1):
        print(i * j, end="\t")
    print()