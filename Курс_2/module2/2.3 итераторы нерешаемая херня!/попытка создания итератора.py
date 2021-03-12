class MyList:
    def __init__(self, lst):
        self.iterable = lst
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            return self.iterable[self.index - 1] / 2
        raise StopIteration

l = MyList([1, 2, 3, 4])
print(type(l))

for i in l:
    print(i)