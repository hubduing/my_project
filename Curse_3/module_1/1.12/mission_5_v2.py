lst = []
for i in range(3):
    lst.append(int(input()))
print(max(lst))
lst.remove(max(lst))
print(min(lst))
lst.remove(min(lst))
print(*lst)