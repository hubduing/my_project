with open("dataset_24465_4 (4).txt") as f, open("polindrom.txt", "w") as x:
    #for line in f:
    #    line = line.rstrip()
    #    line = line[::-1]
    #    line += '\n'
    #    x.write(line)

    a = [i.rstrip() for i in f]
    a.reverse()
    for i in a:
        x.write(i + '\n')
    f.close()
    x.close()