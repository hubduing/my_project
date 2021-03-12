def closest_mod_5(x):
    y = x
    while True:
        if y >= x and y % 5 == 0:
            return y
        y += 1
    return "I don't know :("
print(closest_mod_5(1))