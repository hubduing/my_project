from itertools import takewhile
import itertools


def is_primes(n):
    if n == 2:
        return True
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def primes():
    a = 2
    yield a
    while True:
        a += 1
        if is_primes(a):
            yield a

print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
