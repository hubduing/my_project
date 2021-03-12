s = "a aa b ss ghd as dg aa a b ss"

str = [x for x in s.split()]
my_dict = {}
for i in set(str):
    my_dict[i] = str.count(i)
print(my_dict)