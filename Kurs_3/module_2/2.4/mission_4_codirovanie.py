#s = input()
#s = "abc"
s = "aaaabbcaa"
total = 1
s = s + '1'
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        total += 1
    else:
        print(s[i], total, sep="", end="")
        total = 1



    #print(s[i], total, sep="", end="")