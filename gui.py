from tkinter import *

# ->  параметры и виджеты окна
root = Tk()
root.title('Потоки чисел')
root.geometry('600x400+200+100')
root.config(bg='LightYellow')


Label(height=2, width=95, bg='OliveDrab').place(x=0, y=15)
Label(height=2, width=2, bg='DarkOrange').place(x=537, y=15)

Label(bg='LightYellow', text='Позитивные числа:', fg='DarkOliveGreen', font='Arial 12 bold').place(x=55, y=65)


lbl_positive = Label()
lbl_positive.config(height=2, width=55, relief=RIDGE, bd=3, font='Arial 11 bold', fg='OliveDrab')
lbl_positive.place(x=55, y=90)

Label(bg='LightYellow', text='Список всех чисел:', fg='DarkOliveGreen', font='Arial 12 bold').place(x=55, y=150)


lbl_nums = Label()
lbl_nums.config(height=2, width=55, relief=RIDGE, bd=3, font='Arial 11 bold', fg='Gray')
lbl_nums.place(x=55, y=175)

Label(bg='LightYellow', text='Негативные числа:', fg='DarkOliveGreen', font='Arial 12 bold').place(x=55, y=250)


lbl_negative = Label()
lbl_negative.config(height=2, width=55, relief=RIDGE, bd=3, font='Arial 11 bold', fg='DarkOrange')
lbl_negative.place(x=55, y=275)


Label(height=2, width=95, bg='OliveDrab').place(x=0, y=365)
Label(height=2, width=2, bg='DarkOrange').place(x=37, y=365)
