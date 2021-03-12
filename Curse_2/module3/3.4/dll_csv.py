import csv
from collections import Counter

a = []
lst = []
with open("Crimes.csv") as csvfile, open("result.csv", "w") as res:
    reader = csv.DictReader(csvfile)

    for row in reader:
        if '2015' in row["Date"]:
            lst.append(row['Primary Type'])
            a = dict(Counter(lst).most_common(1))

    writer = csv.writer(res)
    writer.writerow(a)
    #print(*dict.keys(a))





    #for i in range(len(lst()):
    #    print(lst.count(lst[i]))

        #collections.Counter(lst)
    #for i in lst:
    #    if i.count(i) > total:
    #        total = i.count(i)
    #print(total)