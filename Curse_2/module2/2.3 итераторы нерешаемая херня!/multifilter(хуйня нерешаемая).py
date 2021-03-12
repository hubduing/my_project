class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return True

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return True

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return True

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.func = funcs
        self.judge = judge
        self.index = 0

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        self.pos, self.neg = 0, 0
        for i in self.iterable:
            self.index += 1
            for j in self.func:
                self.pos = j(self.iterable[self.index - 1])

            return self.pos
class proverka:
    # Класс для проверки, в решение его вставлять не надо.
    def mul2(x):
        return x % 2 == 0

    def mul3(x):
        return x % 3 == 0

    def mul5(x):
        return x % 5 == 0

    a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

    multifilter1 = multifilter(a, mul2, mul3, mul5)
    # Здесь и дальше создаем разные экземпляры класса. iterable=a, *funcs=[mul2,mul3,mul4]
    multifilter2 = multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)
    multifilter3 = multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)

    print(list(multifilter1))
    # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

    print(list(multifilter2))
    # [0, 6, 10, 12, 15, 18, 20, 24, 30]

    print(list(multifilter3))
    # [0, 30]
