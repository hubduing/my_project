# put your python code here
# получение n, k
z, x = map(int, input().split())

def func(n, k):
    if k > n:
        return 0
    if k == 0:
        return 1
    else:
        return func(n - 1, k) + func(n - 1, k - 1)

print(func(z, x))