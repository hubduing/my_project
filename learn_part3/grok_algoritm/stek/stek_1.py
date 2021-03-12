def greet2(name):
    print('how are you, ' + name + '?')
def bye():
    print('ok bye!')

def greet(name):
    print('Hello, ' + name + '!')
    greet2(name)
    print('getting ready to say bye')
    bye()

i = input('Введи имя: ')
greet(i)