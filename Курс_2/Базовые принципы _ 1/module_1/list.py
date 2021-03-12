x = [1, 2, 3]
y = x
print(y is x) # True
x.append(4)
print(x) # [1, 2, 3, 4]
print(y) # [1, 2, 3, 4]