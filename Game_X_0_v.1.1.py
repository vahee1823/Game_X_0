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

    def print_board(self):
        for cell in self.cells:
            if cell.number % 3 != 0:
                print(f' {cell.status} |', end='')
            else:
                print(f' {cell.status} ')
                print('------------')

    def end_of_game(self, view):
        win1 = [self.cells[0].status, self.cells[1].status, self.cells[2].status]
        win2 = [self.cells[3].status, self.cells[4].status, self.cells[5].status]
        win3 = [self.cells[6].status, self.cells[7].status, self.cells[8].status]
        win4 = [self.cells[0].status, self.cells[3].status, self.cells[6].status]
        win5 = [self.cells[1].status, self.cells[4].status, self.cells[7].status]
        win6 = [self.cells[2].status, self.cells[5].status, self.cells[8].status]
        win7 = [self.cells[0].status, self.cells[4].status, self.cells[8].status]
        win8 = [self.cells[2].status, self.cells[4].status, self.cells[6].status]
        if [view] * 3 in [win1, win2, win3, win4, win5, win6, win7, win8]:
            return 1
        elif set([self.cells[i].status for i in range(9)]) & {1, 2, 3, 4, 5, 6, 7, 8, 9} == set():
            return 2
        else:
            return 0


class Player:
    def __init__(self, name, view):
        self.name = name
        self.view = view

    def go(self, board1, number):  # проверяем занятость клетки и делаем ход
        if board1.cells[number].status != '0' and board1.cells[number].status != 'x':
            board1.cells[number].status = self.view
            return True
        else:
            print('Данная клетка занята! ')
            return False


print('Это игра Крестики-нолики v. 1.1. Первый игрок - крестик, второй - нолик')
board = Board()
player1 = Player(input('Введите имя первого игрока: '), 'x')
player2 = Player(input('Введите второго первого игрока: '), '0')
while True:
    board.print_board()
    a = False
    while not a:
        hod = int(input(f'Ходит игрок {player1.name} Введите номер: ')) - 1
        a = player1.go(board, hod)

    if board.end_of_game('x') == 1:
        board.print_board()
        print(f'Выиграл игрок {player1.name}')
        break
    elif board.end_of_game('x') == 2:
        board.print_board()
        print('Ничья!')
        break

    board.print_board()
    a = False
    while not a:
        hod = int(input(f'Ходит игрок {player2.name} Введите номер: ')) - 1
        a = player2.go(board, hod)

    if board.end_of_game('0'):
        print(f'Выиграл игрок {player2.name}')
        break
    elif board.end_of_game('0') == 2:
        print('Ничья!')
        break
