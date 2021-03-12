with open("dataset_3363_4.txt") as f, open("result_m3", "w") as result:
    total = 0
    dump = []
    res = []
    mat, fiz, rus = 0, 0, 0
    for _ in f:
        s = f.readline().strip()
        total += 1
        dump.append(s.split(';'))
    for i in dump:
        res.append((int(i[1]) + int(i[2]) + int(i[3])) / 3)
        mat += int(i[1])
        fiz += int(i[2])
        rus += int(i[3])
    for i in res:
        print(i)
    res.clear()
    res.append(mat / total)
    res.append(fiz / total)
    res.append(rus / total)
    print(*res)