figura = input()
if figura == "треугольник":
    a, b, c = int(input()), int(input()), int(input())
    p = (a + b + c) / 2
    print(((p * (p - a) * (p - b) * (p - c)) ** 0.5))
elif figura == "прямоугольник":
    a, b = int(input()), int(input())
    print(a * b)
elif figura == "круг":
    r = int(input())
    print(3.14 * (r ** 2))