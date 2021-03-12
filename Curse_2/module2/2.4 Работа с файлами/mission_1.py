f = open("test.txt")
# x = f.read() # считает весь файл целиком
# print(repr(x)) # представление строки 'First line\nSecond Line\nThird Line'
# print(x.splitlines())   # метод разделяет текст на строки, при этом уюирая символ переноса строки
                        # ['First line', 'Second Line', 'Third Line']
x = f.readline() #считывает файл построчно
print(x) # выведет строку с символом переноса, для того что бы его убрать используется rstrip()
print(x.rstrip()) # или при вызове метода: readline().rstrip()

f.close()