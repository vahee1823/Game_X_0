from tkinter import *


def create_x(x, y):  # функция быстрого создания крестика
    canv.create_line(x + 3, y + 3, x + 165, y + 165, width=3, fill='red')
    canv.create_line(x + 165, y + 2, x + 2, y + 165, width=3, fill='red')


def create_o(x, y):  # Функция быстрого создания нолика
    canv.create_oval(x + 3, y + 3, x + 165, y + 165, width=3, outline='blue')


root = Tk()  # Создание и настройка окна
root.geometry('600x650')
root.title('Крестики-нолики 2.0 НЕ РАБОТАЕТ')
root.resizable(False, False)

canv = Canvas(width=501, height=501, bg='#bfbfbf')  # Создание и настройка Canvas
canv.pack()

Sqrt1 = canv.create_rectangle(0, 0, 167, 167, width=3)  # Создание доски (каждого поля)
Sqrt2 = canv.create_rectangle(167, 0, 334, 167, width=3)
Sqrt3 = canv.create_rectangle(334, 0, 504, 167, width=3)
Sqrt4 = canv.create_rectangle(0, 167, 167, 334, width=3)
Sqrt5 = canv.create_rectangle(167, 167, 334, 334, width=3)
Sqrt6 = canv.create_rectangle(334, 167, 504, 334, width=3)
Sqrt7 = canv.create_rectangle(0, 334, 167, 504, width=3)
Sqrt8 = canv.create_rectangle(167, 334, 334, 504, width=3)
Sqrt9 = canv.create_rectangle(334, 334, 504, 504, width=3)


root.mainloop()  # Зацикливание окна (конец программы)
