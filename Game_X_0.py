from tkinter import *
from tkinter import messagebox


class Cell:
    def __init__(self, number, status):
        self.number = number
        self.status = status


class Board:
    def __init__(self):
        self.cells = []
        for i_cell in range(1, 10):
            cell = Cell(i_cell, i_cell)
            self.cells.append(cell)

    def end_of_game(self, view):
        win1 = [self.cells[0].status, self.cells[1].status, self.cells[2].status]
        win2 = [self.cells[3].status, self.cells[4].status, self.cells[5].status]
        win3 = [self.cells[6].status, self.cells[7].status, self.cells[8].status]
        win4 = [self.cells[0].status, self.cells[3].status, self.cells[6].status]
        win5 = [self.cells[1].status, self.cells[4].status, self.cells[7].status]
        win6 = [self.cells[2].status, self.cells[5].status, self.cells[8].status]
        win7 = [self.cells[0].status, self.cells[4].status, self.cells[8].status]
        win8 = [self.cells[2].status, self.cells[4].status, self.cells[6].status]
        winlist = [win1, win2, win3, win4, win5, win6, win7, win8]
        # if [view] * 3 in [win1, win2, win3, win4, win5, win6, win7, win8]:
        #     return 1
        if [view] * 3 in [win1, win2, win3, win4, win5, win6, win7, win8]:
            for i in range(len(winlist)):
                if [view] * 3 == winlist[i]:
                    return 1, i
        if set([self.cells[i].status for i in range(9)]) & {1, 2, 3, 4, 5, 6, 7, 8, 9} == set():
            return 2,
        else:
            return 0,


class Player:
    def __init__(self, view):
        self.view = view

    def go(self, board1, number):  # проверяем занятость клетки и делаем ход
        try:
            if board1.cells[number].status != '0' and board1.cells[number].status != 'x':
                board1.cells[number].status = self.view
                ErrorLabel.config(text='Приятной игры!', fg='black')
                return True
            else:
                ErrorLabel.config(text='Данная клетка занята! ', fg='red')
                return False
        except IndexError:
            ErrorLabel.config(text='Ошибка 01: IndexError.\n Сделайте скриншот игры и отправьте его создателю',
                              bg='red', fg='white', font='Consolas, 14')
            return False


def create_x(x, y):  # функция быстрого создания крестика
    canv.create_line(x + 3, y + 3, x + 165, y + 165, width=3, fill='red')
    canv.create_line(x + 165, y + 2, x + 2, y + 165, width=3, fill='red')


def create_o(x, y):  # Функция быстрого создания нолика
    canv.create_oval(x + 3, y + 3, x + 165, y + 165, width=3, outline='blue')


def click(objct):  # Обработчик нажатия на блок (поле)
    global latest, canv, SqrtList, win
    if not win:
        if latest == 'x':  # Если последний ход x то ходит 0
            if player2.go(board, SqrtList.index(objct)):
                create_o(canv.coords(objct)[0], canv.coords(objct)[1])
                InfoLabel.config(text='Ходит игрок 1 (X)')
                latest = '0'
        elif latest == '0':  # Если последний ход 0, то ходит x
            if player1.go(board, SqrtList.index(objct)):
                create_x(canv.coords(objct)[0], canv.coords(objct)[1])
                InfoLabel.config(text='Ходит игрок 2 (О)')
                latest = 'x'
        if board.end_of_game(latest)[0] == 1:  # Если игру выиграл один из игроков
            eog167 = 167 * board.end_of_game(latest)[1]
            if 2 < board.end_of_game(latest)[1] < 6:
                eog167 = eog167 - 167 * 3
            if board.end_of_game(latest)[1] < 3:  # Зачёркиваем комбо
                canv.create_line(68, 83 + eog167, 433, 83 + eog167, width=3)
            elif board.end_of_game(latest)[1] < 6:
                canv.create_line(83 + eog167, 71, 83 + eog167, 433, width=3)
            elif board.end_of_game(latest)[1] == 6:
                canv.create_line(68, 68, 433, 433, width=3)
            elif board.end_of_game(latest)[1] == 7:
                canv.create_line(68, 433, 433, 68, width=3)
            else:
                print('kj[')
            if latest == 'x':  # Последний x => победил игрок 1
                print(board.end_of_game(latest))
                InfoLabel.config(text='Выиграл Игрок 1!')
                ErrorLabel.config(text='Может ещё разок?')
                root.title('Игрок 1 победил!')
                messagebox.showinfo('Игра окончена', 'Игрок 1 победил!')
                win = True
            else:  # Иначе победил игрок 2
                InfoLabel.config(text='Выиграл Игрок 2!')
                ErrorLabel.config(text='Может ещё разок?')
                root.title('Игрок 2 победил!')
                messagebox.showinfo('Игра окончена', 'Игрок 2 победил!')
                win = True
        elif board.end_of_game(latest)[0] == 2:  # Ничья
            InfoLabel.config(text='Ничья!')
            ErrorLabel.config(text='Может ещё разок?')
            root.title('Ничья!')
            messagebox.showinfo('Ничья!', 'К сожалению, никто не выиграл')
            win = True
        if win:
            ReplayBut = Button(text='НЕТ', command='')
            ReplayBut.pack()


def change_color(obj, color):
    obj.config(bg=color)


def sqrt_change_color(sqrlist, c, color):
    for obj in sqrlist:
        c.itemconfig(obj, fill=color)
    if color == 'black':
        for obj in sqrlist:
            c.itemconfig(obj, outline='white')
    else:
        for obj in sqrlist:
            c.itemconfig(obj, outline='black')


root = Tk()  # Создание и настройка окна
root.geometry('600x700')
root.title('Крестики-нолики v. 2.2')
root.resizable(False, False)

TitleLabel = Label(text='Это игра Крестики-нолики v. 2.2\n Первый игрок - крестик, второй - нолик',
                   font='Consolas, 14')
TitleLabel.pack()

canv = Canvas(width=501, height=501, bg='#bfbfbf')  # Создание и настройка Canvas.
canv.pack()

Sqrt1 = canv.create_rectangle(0, 0, 167, 167, width=3, fill='#bfbfbf')  # Создание доски (каждого поля)
Sqrt2 = canv.create_rectangle(167, 0, 334, 167, width=3, fill='#bfbfbf')
Sqrt3 = canv.create_rectangle(334, 0, 504, 167, width=3, fill='#bfbfbf')
Sqrt4 = canv.create_rectangle(0, 167, 167, 334, width=3, fill='#bfbfbf')
Sqrt5 = canv.create_rectangle(167, 167, 334, 334, width=3, fill='#bfbfbf')
Sqrt6 = canv.create_rectangle(334, 167, 504, 334, width=3, fill='#bfbfbf')
Sqrt7 = canv.create_rectangle(0, 334, 167, 504, width=3, fill='#bfbfbf')
Sqrt8 = canv.create_rectangle(167, 334, 334, 504, width=3, fill='#bfbfbf')
Sqrt9 = canv.create_rectangle(334, 334, 504, 504, width=3, fill='#bfbfbf')
SqrtList = [Sqrt1, Sqrt2, Sqrt3, Sqrt4, Sqrt5, Sqrt6, Sqrt7, Sqrt8, Sqrt9]

InfoLabel = Label(text='Начинает игрок 1 (X)', font='Consolas, 24')
InfoLabel.pack()

ErrorLabel = Label(text='Приятной игры', font='Consolas, 20')
ErrorLabel.pack()

win = False

board = Board()
player1 = Player('x')
player2 = Player('0')
latest = '0'

canv.tag_bind(Sqrt1, '<Button-1>', lambda obj=Sqrt1: click(Sqrt1))
canv.tag_bind(Sqrt2, '<Button-1>', lambda obj=Sqrt2: click(Sqrt2))
canv.tag_bind(Sqrt3, '<Button-1>', lambda obj=Sqrt3: click(Sqrt3))
canv.tag_bind(Sqrt4, '<Button-1>', lambda obj=Sqrt4: click(Sqrt4))
canv.tag_bind(Sqrt5, '<Button-1>', lambda obj=Sqrt5: click(Sqrt5))
canv.tag_bind(Sqrt6, '<Button-1>', lambda obj=Sqrt6: click(Sqrt6))
canv.tag_bind(Sqrt7, '<Button-1>', lambda obj=Sqrt7: click(Sqrt7))
canv.tag_bind(Sqrt8, '<Button-1>', lambda obj=Sqrt8: click(Sqrt8))
canv.tag_bind(Sqrt9, '<Button-1>', lambda obj=Sqrt9: click(Sqrt9))
# canv.coords(Sqrt1)

m = Menu(root)  # Создание меню
vidm = Menu(m)
polefontm = Menu(vidm)
root.config(menu=m)
m.add_cascade(label='Вид', menu=vidm)
vidm.add_cascade(label='Изменить фон поля', menu=polefontm)
polefontm.add_command(label='Серый (обычный)', command=lambda c='#bfbfbf': sqrt_change_color(SqrtList, canv, c))
polefontm.add_command(label='Тёмный режим', command=lambda c='#2b2b2b': sqrt_change_color(SqrtList, canv, c))
polefontm.add_command(label='Чёрный', command=lambda c='black': sqrt_change_color(SqrtList, canv, c))
polefontm.add_command(label='Оранжевый', command=lambda c='#ff9920': sqrt_change_color(SqrtList, canv, c))
polefontm.add_command(label='Жёлтый', command=lambda c='yellow': sqrt_change_color(SqrtList, canv, c))
polefontm.add_command(label='Зелёный', command=lambda c='green': sqrt_change_color(SqrtList, canv, c))
polefontm.add_command(label='Голубой', command=lambda c='#4fe8fa': sqrt_change_color(SqrtList, canv, c))
polefontm.add_command(label='Пурпурный', command=lambda c='#8D6FF0': sqrt_change_color(SqrtList, canv, c))
polefontm.add_command(label='Белый', command=lambda c='white': sqrt_change_color(SqrtList, canv, c))

root.mainloop()  # Зацикливание окна (конец программы)
