try: # пробуй запустить
    x = [1, 2, 'hello!', 3]
    x.sort()
    print(x)
except TypeError: # указываем тип ошибка
    print('Type error :( ') # указываем что сделать в случае ошибки

print('i can catch')