class MyList:
    def __init__(self, lst, func):
        self.iterable = lst
        self.func = func
        self.index = 0

    def judge(self, num):
        return "element = " + str(num)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            self.result_of_f2 = self.func(self.iterable[self.index - 1])
            self.result_of_judge = self.judge(self.result_of_f2)
            return self.result_of_judge
        raise StopIteration


def f2(n):
    return n / 2

l = MyList([1, 2, 3, 4, 5], f2)

for i in l:
    print(i)