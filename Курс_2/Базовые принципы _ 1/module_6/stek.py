class ExtendedStack(list):
    def sum(self):
        # операция сложения
        self.append(self.pop() + self.pop())
    def sub(self):
        # операция вычитания 
        self.append(self.pop() - self.pop())
    def mul(self):
        # операция умножения
        self.append(self.pop() * self.pop())
    def div(self):
        # операция целочисленного деления
        self.append(self.pop() // self.pop())

#l=  [1, 2, 3, 4, 5, 6, 7, 8, 9, 2]
#x = ExtendedStack(l)
#x.sum()