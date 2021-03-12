def f(x, y):
    try:
        return x / y
    except TypeError:
        print('Type error')
    except ZeroDivisionError:
        print('Не делится на ноль!')

#f(5, []) #tyoe error
f(5, 0) # ZeroDivisionError: division by zero