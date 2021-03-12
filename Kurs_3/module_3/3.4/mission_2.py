my_dict = {}
total = 0
total2 = 0
a = ""
with open("dataset_3363_3.txt") as f:
    s = f.read().replace('\n', ' ').lower().split()
    s.sort()
    for j in s:
        if s.count(j) > total2:
            total2 = s.count(j)
            a = j

    for i in s:
        if total < s.count(i):
            total = s.count(i)
            my_dict[i] = s.count(i)
print(a, total2, end="\n_____________\n")

for k,v in my_dict.items():
    print(k, v)
