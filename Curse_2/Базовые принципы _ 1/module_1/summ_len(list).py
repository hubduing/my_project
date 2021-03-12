def sum_len_list(n):
    m = []
    ans = 0
    for i in n:
        if id(i) not in m:
            m.append(id(i))
            ans += 1
    return ans

n = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]
print(sum_len_list(n))