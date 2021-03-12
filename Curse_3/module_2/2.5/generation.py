a = [0] * 5
print(a, end="\n\n")

a = [0 for i in range(5)]
print(a, end="\n\n")

a = [i*i for i in range(5)]
print(a, end="\n\n")

a = [int(i) for i in input().split()]
print(a)