#'Голосование'
voted = {}
def check_voter(name):
    if voted.get(name):
        print('Kick them out!')
    else:
        voted[name] = True
        print('Let them vote!')
n = int(input('Введите количество человек:'))
for i in range(n):
    names = input('Введите имя человека: ')
    check_voter(names)