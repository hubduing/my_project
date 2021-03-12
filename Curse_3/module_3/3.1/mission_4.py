def modify_list(*l):
    lst = []
    for i in l:
        print(i, end=" ")
        if int(i) % 2 == 0:
            lst.append(int(i) // 2)
    for y in lst:
        if y % 2 == 1:
            modify_list(lst)
        else:
            return lst

#print(modify_list(1, 2, 3, 4, 5, 6))
print(modify_list(10, 5, 8, 3))