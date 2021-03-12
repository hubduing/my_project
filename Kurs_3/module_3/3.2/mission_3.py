n = int(input())
my_dict = {}
for i in range(n):
    a = int(input())
    if a in my_dict:
        print(my_dict[a])
    else:
        my_dict[a] = f(a)
        print(my_dict[a])