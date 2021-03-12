string = input()
#acggtgttat
sum1 = string.upper().count("G")
sum2 = string.upper().count("C")
print((float(sum1) + float(sum2))/len(string) * 100)
