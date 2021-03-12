

def greet(name):
    if name[0].isupper():
        return 'Hello, ' + name
    else:
        raise ValueError(name + "is inappropriate name")

while True:
    try:
        name = input('Please enter your name: ')
        greetting = greet(name)
        print(greetting)
    except ValueError:
        print('Please try again')
    else:
        break