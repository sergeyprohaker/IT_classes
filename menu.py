from tkinter import *
import math
f1 = Tk()
f1.geometry('400x400')


def task3():
    def change_bg1():
        f3['bg'] = 'red'

    def change_size():
        f3.geometry('700x700')
    f3 = Tk()
    f3.geometry('400x400')
    put = Button(f3, text='Изменить цвет формы', command=lambda: change_bg1())
    put1 = Button(f3, text='Изменить размер формы', command=lambda: change_size())
    put.place(x=150, y=150)
    put1.place(x=140, y=180)
    f3.mainloop()


def task2():
    def clear():
        l100500['text'] = ''
    f4 = Tk()
    f4.geometry('400x400')
    l100500 = Label(f4, text='Это вроде поле Memo, только оно и так для чтения' + '\n' + 'поэтому сделаю только очистку')
    l100500.place(x=50, y=150)
    tyk = Button(f4, text='Очистить', command=lambda: clear())
    tyk.place(x=150, y=250)
    f4.mainloop()


def change_bg():
    f1['bg'] = 'blue'
    f1.geometry('700x700')


def click_button():
    f2 = Tk()
    f2.geometry('500x500')
    l = Label(f2, text='X1')
    l1 = Label(f2, text='Y1')
    l2 = Label(f2, text='X2')
    l3 = Label(f2, text='Y2')
    l4 = Label(f2, text='X3')
    l5 = Label(f2, text='Y3')
    e = Entry(f2, width=20)
    e1 = Entry(f2, width=20)
    e2 = Entry(f2, width=20)
    e3 = Entry(f2, width=20)
    e4 = Entry(f2, width=20)
    e5 = Entry(f2, width=20)
    e.place(x=30, y=10)
    e1.place(x=30, y=40)
    e2.place(x=30, y=70)
    e3.place(x=30, y=100)
    e4.place(x=30, y=130)
    e5.place(x=30, y=160)
    l.place(x=10, y=10)
    l1.place(x=10, y=40)
    l2.place(x=10, y=70)
    l3.place(x=10, y=100)
    l4.place(x=10, y=130)
    l5.place(x=10, y=160)

    def t1():
        x1 = int(e.get())
        y1 = int(e1.get())
        x2 = int(e2.get())
        y2 = int(e3.get())
        x3 = int(e4.get())
        y3 = int(e5.get())
        a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        b1 = math.sqrt((x3-x2)**2 + (y3-y2)**2)
        c = math.sqrt((x1-x3)**2 + (y1-y3)**2)
        if a + b1 <= c or a + c <= b1 or b1 + c <= a:
            l9 = Label(f2, text='Треугольник не существует')
            l9.place(x=300, y=220)
        else:
            p = a + b1 + c
            pp = p / 2
            s = math.sqrt(pp * (pp - a) * (pp - b1) * (pp - c))
            l6 = Label(f2, text='Сторона 1: ' + str(a))
            l7 = Label(f2, text='Сторона 2: ' + str(b1))
            l8 = Label(f2, text='Сторона 3: ' + str(c))
            l6.place(x=300, y=120)
            l7.place(x=300, y=150)
            l8.place(x=300, y=180)
            ang1 = math.cos(b1 ** 2 + c ** 2 - a ** 2) / (2 * b1 * c)
            ang2 = math.cos(a ** 2 + c ** 2 - b1 ** 2) / (2 * a * c)
            ang3 = math.cos(a ** 2 + b1 ** 2 - c ** 2) / (2 * a * b1)
            l11 = Label(f2, text='Угол 1: ' + str(math.degrees(math.acos(ang1))))
            l12 = Label(f2, text='Угол 2: ' + str(math.degrees(math.acos(ang2))))
            l13 = Label(f2, text='Угол 3: ' + str(math.degrees(math.acos(ang3))))
            l11.place(x=300, y=280)
            l12.place(x=300, y=310)
            l13.place(x=300, y=340)
            l10 = Label(f2, text='Периметр: ' + str(p) + '\n' + 'Площадь: ' + str(s))
            l10.place(x=300, y=220)
    but = Button(f2, text='Посчитать', command=lambda: t1())
    but.place(x=300, y=10)
    f2.mainloop()


b = Button(f1, text='Треугольник', command=click_button)
b.place(x=20, y=20)
b2 = Button(f1, text='Настройки', command=lambda: change_bg())
b2.place(x=20, y=50)
b3 = Button(f1, text='Задание 3', command=lambda: task3())
b3.place(x=150, y=20)
b4 = Button(f1, text='Задание 2', command=lambda: task2())
b4.place(x=280, y=20)
f1.mainloop()
