def f(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e:
        print(type(e)) # узнали тип объекта ошибки - <class 'ZeroDivisionError'>
        print(e) # вывели саму ошибку - division by zero
        print(e.args) # аргумент ошибки - ('division by zero',)
 
f(5, 0)
f(5, [])