arr = {}
def telefon_hesh(name):
    if arr.get(name):
        print('Уже есть такое имя!')
        return
    else:
        number = int(input('Введите номер телефона: '))
        arr[name] = number
    print(arr)
while True:
    names = input('Введите имя человека: ')
    telefon_hesh(names)
    print()
    end = input('Продолжить? (что бы выйти - "нет")')
    if end == 'нет':
        break