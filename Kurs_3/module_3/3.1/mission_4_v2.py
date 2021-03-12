def modify_list(l):
    res = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i] //= 2
            res.append(l[i])
    alpha = []
    for x in res:
        if len(res) == 1:
            return x
        if x % 2 == 0:
            modify_list()

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))