def update_dictionary(d, key, value):
    if key in d:
        d[key] = [value]
    else:
        d[2 * key] = [value]
    return d