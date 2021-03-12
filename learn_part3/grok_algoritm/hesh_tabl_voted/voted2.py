#'Голосование'
voted = {}
def check_voter(name):
    if voted.get(name):
        print('Гоните его!')
    else:
        voted[name] = True
        print('Пустить к голосованию!')
while True:

    names = input('Введите имя человека: ')
    check_voter(names)
    print()
    end = input('Продолжить? (нет - выход)')
    if end == 'нет':
        break