def min_f(*a):
    m = a[0]
    for x in a:
        if x < m:
            m = x
    return m
print(min_f(10, 4, 2, 5, 7))
