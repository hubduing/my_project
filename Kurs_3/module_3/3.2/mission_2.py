#str = input()
#a aa abC aa ac abc bcd a
s = "a aa abC aa ac abc bcd a"
#str = [i for i in input().lower().split()]
str = [i for i in s.split()]
#my_dict = {}
#for i in set(str):
#    my_dict[i] = str.count(i)

#str = [i for i in input().lower().split()]
my_dict = {}
for i in set(str):
    my_dict[i] = str.count(i)
for key, value in my_dict.items():
    print(key, value)