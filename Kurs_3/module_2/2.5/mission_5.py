string = [i for i in input().split()]
res = []
for i in string:
    if string.count(i) > 1:
        if i not in res:
            res.append(i)
print(*res)


#print(string)