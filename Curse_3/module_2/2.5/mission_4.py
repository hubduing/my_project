#string = [1, 3, 5, 6, 10]
string = [int(i) for i in input().split()]
if len(string) == 1:
    print(*string)
elif len(string) == 2:
    for i in range(len(string)):
        if i == 0:
            print((string[-1] + string[1]), end=" ")
        elif i == 1:
            print((string[-2] + string[0]), end=" ")
else:
    for i in range(len(string)):
        if i == 0:
            print((string[-1] + string[1]), end=" ")
        elif i == len(string) - 1:
            print((string[-2] + string[0]), end=" ")
        else:
            print(string[i - 1] + string[i + 1], end=" ")
