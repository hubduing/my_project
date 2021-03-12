import datetime
def date_vanga():
    #получаем дату и кол-во дней
    (y, m, d) = [int(n) for n in input().split()]
    day_time = int(input())

    date = datetime.date(y, m, d) # полученную дату переводим в тип дата
    delta = datetime.timedelta(days=day_time) # находим промежуток времени
    delta = date + delta
    total = 0
    #delta = delta.strftime('%Y %-m %-d')
    #print(delta.strftime('%Y %m %d'))
    d = delta.timetuple()
    for i in d:
        print(i, end=' ')
        total += 1
        if total == 3:
            break

date_vanga()
# 2000 02 05