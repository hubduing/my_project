a, b, c = int(input()), int(input()), int(input())

if a >= b:
    print(a)
    if b >= c:
        print(c)
        print(b)
    else:
        print(b)
        print(c)
else:
    print(b)
    if a >= c:
        print(c)
        print(a)
    else:
        print(a)
        print(c)
if b >= c:
    print(b)
    if a >= c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
else:
    print(c)
    if a >= c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
if a >= c:
    print(a)
    if b >= c:
        