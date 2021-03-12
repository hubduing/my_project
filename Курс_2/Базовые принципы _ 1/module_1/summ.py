def summa(num):
    sum = 0
    for _ in range(num):
        num = int(input())
        sum += num
    return sum
number = int(input())
print(summa(number))