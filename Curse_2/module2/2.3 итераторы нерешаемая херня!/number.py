from math import sqrt

def prost(number):
    a = range(number + 1)
    print(a[1])
    a[1] = 0
    lst = []
    i = 2
    while i <= number:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, number + 1, i):
                a[j] = 0
        i += 1
print(prost(40))