def divine(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by error')
    else:
        print('result is ', result)
    finally:
        print('finally')
divine(2, 1)
divine(2, 0)
divine(2, [])