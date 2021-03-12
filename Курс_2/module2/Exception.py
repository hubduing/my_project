
print('This line is executed')
class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0
class MyList(list, EvenLengthMixin):
    pass
ml = MyList([2, 4, 1, 3])
#ml = MyList([2, 'abc', 4, 1, 3]) # type error
ml.sort()
print(ml)


#x = [1, 2, 3]
#print(x[4]) # IndexError: list index out of range

def f():
    x = [1, 2, 3]
    print(x[4]) # line 18, in <module> f()
                # line 17, in f print(x[4])
f()
