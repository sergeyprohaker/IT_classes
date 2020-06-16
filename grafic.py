from tkinter import *


def t1():
    a = int(EA.get())
    b = int(EB.get())
    c = int(EC.get())
    d = int(ED.get())
    e = int(EE.get())
    f2 = Tk()
    canvas = Canvas(f2, bg='white', height=600, width=600)
    p1 = (0.0, 300.0),
    p2 = (600, 300)
    p3 = (300.0, 0.0),
    p4 = (300, 600)
    canvas.create_line(p1, p2, fill='black')
    canvas.create_line(p3, p4, fill='black')
    s = []
    for x in range(-300, 300, 1):
        y = - (a * (x ** 4) + b * (x ** 3) + c * (x ** 2) + d * x + e)
        x1 = x + 300
        y1 = y // 100 + 300
        f = (x1, y1)
        s.append(f)
        print(s)
    canvas.create_line(*s, fill='blue')
    canvas.pack()


f1 = Tk()
f1.geometry('400x400')
l1 = Label(f1, text='Введите коэффициенты a,b,c,d,e')
l1.place(x=5, y=5)
EA = Entry(f1, width=10)
EA.place(x=10, y=50)
EB = Entry(f1, width=10)
EB.place(x=10, y=90)
EC = Entry(f1, width=10)
EC.place(x=10, y=130)
ED = Entry(f1, width=10)
ED.place(x=10, y=170)
EE = Entry(f1, width=10)
EE.place(x=10, y=210)
but = Button(f1, text='Draw graph', command=t1)
but.place(x=250, y=70)
f1.mainloop()
