class Buffer:
    def __init__(self): # конструктор без аргументов
        self.buffer = []
    def add(self, *a): # добавить следующую часть последовательности
        self.total = 0
        self.buffer += a
        self.buffer_end = []

        if len(self.buffer) == 5:
            self.buffer = self.buffer[:5]
            for i in self.buffer:
                self.total += i
            print(self.total)
            self.buffer_end = []
        if len(self.buffer) < 5:
            self.buffer = self.buffer[:5]
            for i in self.buffer:
                self.total += i
            print(self.total)
            self.buffer_end = self.buffer
        else:
            self.buffer_end = self.buffer[5:]
            for i in self.buffer[:5]:
                self.total += i
            print(self.total)
            self.buffer = []
            self.buffer += self.buffer_end

    def get_current_part(self):
    # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        print(self.buffer_end)
        #return self.buffer_end

buf = Buffer()
buf.add(1, 2, 3) # 6
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]