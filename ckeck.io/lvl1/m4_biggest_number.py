def max_digit(number: int) -> int:
    # your code here
    minim = 0
    if number == 0:
        return 0
    else:
        while number != 0:
            last = number % 10
            if minim < last:
                minim = last
            number //= 10
        return minim

if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
