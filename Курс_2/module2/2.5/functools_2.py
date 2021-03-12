from functools import reduce, partial

def orderFunc(a, b, c, d):
    # return a * 4 + b * 3 + c * 2 + d
    print(a, b, c, d)

result = partial(orderFunc, 1, d=4) # 1 ушло вмсето а (первая), а 4 вместо d (последняя)
result(2, 3)  # 1 2 3 4

result = partial(orderFunc, 1, с=4) # попытаемся подставить 4 в середину вмсето с
result(2, 3) # Я предполагаю, что orderFunc вызовется вот так orderFunc(1, 2, 4, 3), но ничего не выходит
# Traceback (most recent call last):
#   File "./Fence.py", line 21, in <module>
#     result(2, 3)
# TypeError: orderFunc() got an unexpected keyword argument 'с'


result = partial(orderFunc, a = 1, с=4) #даже если всё сделать поименованным, получим то же самое
result(2, 3)
# Traceback (most recent call last):
#   File "./Fence.py", line 21, in <module>
#     result(2, 3)
# TypeError: orderFunc() got multiple values for argument 'a'

result = partial(orderFunc, a=1, c=4, d=1)  # НЕЕЕЕТ то что подставляется в начало должно быть без имен, а то, что в конец только с именами
result(2)
# Traceback (most recent call last):
#   File "./Fence.py", line 21, in <module>
#     result(2)
# TypeError: orderFunc() got multiple values for argument 'a'