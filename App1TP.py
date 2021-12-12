
from tkinter import *
from tkinter import messagebox
import sys


x = []
y = []



def get_all():  
    try:
        valuex = int(xname.get())
    except ValueError:
        message=messagebox.showinfo(("Ошибка"), ("Введите целое число"))
    x.append(valuex)
    print('x:',x)

    try:
        valuey = int(yname.get())
    except ValueError:
        message=messagebox.showinfo(("Ошибка"), ("Введите целое число"))
    y.append(valuey)
    print('y:',y)

def del_array():
#отчистка массивов, содержащих внутри себя данные, введённых точек
#отчистка холста
    x.clear()
    y.clear()
    canvas.delete("all")

def draw_function():
#построение линий на графике
    global x, y
    cornersnumb = len(x)
    if (cornersnumb < 3):
        message=messagebox.showinfo(("Ошибка"), ("Многоугольник не может содержать менее 3 углов"))
    else:
        for i in range (cornersnumb):
            canvas.create_line(x[i-1], y[i-1], x[i], y[i])

def S_function():
    #подсчёт площади
    global x, y
    cornersnumb= len(x)
    S1 = 0 
    for i in range (cornersnumb):
        Sum=x[i-1]*y[i]-x[i]*y[i-1]
        S1+=Sum
    S = float()
    S = abs(0.5 * S1)
    print(S)
    S = str(S)
    mytext = 'Площадь многоугольника: '+ S
    print(type(mytext))
    text = Label(win, text = str(S), width=25, height=5).grid(row=4, column=1)

def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        win.destroy()

def vyp_function():
    #определение выпуклости
    global x, y
    cornersnumb= len(x)
    PosAngle = False
    NegAngle = False
    for i in range(cornersnumb):
        x1 = x[i]
        y1 = y[i]
        x2 = x[(i+1) % cornersnumb]
        y2 = y[(i+1) % cornersnumb]
        x3 = x[(i+2) % cornersnumb]
        y3 = y[(i+1) % cornersnumb]
        d = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)
        if d > 0:
            PosAngle = True
        elif d < 0:
            NegAngle = True
    if PosAngle and NegAngle:
        res = 'Многоугольник не выпуклый'
        #res=print("Многоугольник не выпуклый")
        text = Label(win, text = str(res), width=25, height=5).grid(row=5, column=1)
    else:
        #res=print("Многоугольник выпуклый")
        #message=messagebox.showinfo(("Результат"), ("Многоугольник выпуклый"))
        res = 'Многоугольник выпуклый'
        text = Label(win, text = str(res), width=25, height=5).grid(row=5, column=1)
    return(res)


win = Tk()# создаём окно
win.protocol("WM_DELETE_WINDOW", on_closing) 
win.title("Подсчёт площади и определение выпуклости многоугольника")
win.geometry('696x1200') #размеры окна и отступы от левого верхнего угла
win.resizable(0,0) #нельзя изменить размер
win.image = PhotoImage(file='cow.png')
bg_logo=Label(win, image=win.image)
bg_logo.grid(rowspan= 24,columnspan =3)

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)
win.grid_columnconfigure(2, minsize=100)
win.grid_columnconfigure(3, minsize=100)
win.grid_columnconfigure(4, minsize=100)
win.grid_columnconfigure(5, minsize=100)

Zagolovokx = Label(win, text = "Введите координату x:").grid(row=0, column =0, stick = "w")
xname = Entry(win)
xname.grid(row=0, column =1)

Zagolovoky = Label(win, text = "Введите координату y:").grid(row=1, column =0, stick = "w")
yname = Entry(win)
yname.grid(row=1, column =1)

Button(win, text="Записать координату", command=get_all).grid(row=1, column =2)

Zagolovokcanvas = Label(win, text = "Полученная фигура:").grid(row=2, column =0, stick = "w")
canvas = Canvas(win, height=200, width=200, background="#AFEEEE")
canvas.grid(row =3, column =0, stick="w")


Button(win, text="Построить график", command= draw_function).grid(row=3, column=1)

Button(win, text="Поcчитать площадь многоугольника", command= S_function).grid(row=4, column=0, stick = "w")

Button(win, text="Определить выпуклость", command= vyp_function).grid(row=5, column=0, stick = "w")

Button(win, text="Очистить координаты", command= del_array).grid(row=7, column=0, stick = "w")



win.mainloop()
sys.exit()


