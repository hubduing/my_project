class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.money = capacity
    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.money >= v:
            return True
        else:
            return False
    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.money -= v
            #print(self.money)
x = MoneyBox(15)
x.add(5)
x.add(9)
x.add(3)