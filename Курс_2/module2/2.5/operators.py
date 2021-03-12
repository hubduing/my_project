import operator as op
'''
print(op.add(4, 5)) # add ~ +
print(op.mul(4, 5)) # mul ~ *
print(op.contains([1, 2, 3], 4)) # 4 in [1, 2, 3] ? if not in -- False

x = [1, 2, 3]
f = op.itemgetter(1) # f(x) == x(1)
print(f(x))
'''
#------------------------
#f = op.attrgetter("sort") # f(x) == x.sort
#print(f([]))
#------------------------
x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
]
x.sort(key=op.attrgetter(-1))
print(x)