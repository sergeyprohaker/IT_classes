from tkinter import *
from math import sqrt


def t1():
    x = int(e.get())
    y = int(e1.get())
    x1 = int(e2.get())
    y1 = int(e3.get())
    x2 = int(e4.get())
    y2 = int(e5.get())
    st1 = sqrt((x1-x)**2 + (y1-y)**2)
    st2 = sqrt((x2-x1)**2 + (y2-y1)**2)
    st3 = sqrt((x2-x)**2 + (y2-y)**2)
    l1 = Label(f1, text='Координаты 1 = ' + str(st1))
    l1.place(x=100, y=200)
    l2 = Label(f1, text='Координаты 2 = ' + str(st2))
    l2.place(x=100, y=250)
    l3 = Label(f1, text='Координаты 3 = ' + str(st3))
    l3.place(x=100, y=300)


f1 = Tk()
f1.geometry('400x400')
e = Entry(f1, width=20)
e1 = Entry(f1, width=20)
e2 = Entry(f1, width=20)
e3 = Entry(f1, width=20)
e4 = Entry(f1, width=20)
e5 = Entry(f1, width=20)
b1 = Button(f1, text='Проверить', command=lambda: t1())
e.place(x=20, y=30)
e1.place(x=20, y=50)
e2.place(x=20, y=70)
e3.place(x=20, y=90)
e4.place(x=20, y=110)
e5.place(x=20, y=130)
b1.place(x=300, y=50)
f1.mainloop()
