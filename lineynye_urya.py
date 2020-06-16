a = float(input("Введите 1 коэфф "))
b = float(input("Введите 2 коэфф "))
c = float(input("Введите 3 коэфф "))
d = float(input("Введите 4 коэфф "))
e = float(input("Введите 5 коэфф "))
f = float(input("Введите 6 коэфф "))
if b != 0:
    y = (c * e - a * f) / (b * c - a * d)
    if c != 0:
        x = (f - d * y) / c
        print(x, y)
else:
    if a != 0:
        x = (f * b - d * e) / (b * c - d * a)
        if d != 0:
            y = (f - c * x) / d
            print(x, y)
