'''
1
-3
5
-6
-10
13
4
-8

'''

num = 0
res = 0

while True:
    number = int(input())
    if number + num == 0:
        res += number ** 2
        print(res)
        break
    else:
        res += number ** 2
        num += number