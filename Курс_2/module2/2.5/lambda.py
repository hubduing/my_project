x = input().split()
xs = (int(i) for i in x)
evens = list(filter(lambda x: x % 2 == 0, xs))
print(evens)