def nearest_value(values: set, one: int) -> int:
    # your code here
    lst = []
    for i in range(max(values) + 1):
        if i in values:
            lst.append(i)
    #print(lst)
    min_v = 0
    max_v = 0
    for j in range(len(lst)):
        if lst[j] <= one <= lst[j + 1]:
            min_v = one - lst[j]
            max_v = lst[j + 1] - one
            if min_v < max_v:
                return min_v
            else:
                return max_v


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
