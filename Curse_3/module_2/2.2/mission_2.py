#Так: range(1, 10) range(20, 30) range(40, 60)
#for i in range(1, 10), range(20, 30), range(40, 60):
#    print(i)
#Так:
a = [i for i in range(1, 10)]
b = [i for i in range(100, 110)]
c = [i for i in range(1000, 1010)]
for i in a, b, c:
    print(i)
#[1, 2, 3, 4, 5, 6, 7, 8, 9]
#[100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
#[1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]