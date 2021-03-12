my_list = []
l = ''
digit = ""
with open("dataset_3363_2.txt") as op:
    for line in op:
        print(line)

        for i in range(len(line)):
            if line[i].isalpha():
                for j in range(i + 1, len(line)):
                    if line[j].isdigit():
                        digit += line[j]
                    else:
                        l += line[i] * int(digit)

                        digit = ""
                        break
    print(l)
