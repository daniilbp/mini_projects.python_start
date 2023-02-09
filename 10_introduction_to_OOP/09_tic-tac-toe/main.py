import random


class Cell:
    def __init__(self, cell, player, cells):
        while True:
            try:
                if cell not in cells:
                    raise ValueError
                break
            except ValueError:
                print('\nКлетка уже занята или введены данные выходящие за рамки игрового поля.')
                cell = input(f'{player.name} введите данные клетки еще раз (пример: 1 1): ').split()
        self.cell = cell
        cells.remove(self.cell)
        print(f'Свободные клетки: {cells}')


class Player:
    def __init__(self, name, cells):
        self.name = name
        self.cells = cells

    def info(self):
        print(f'Занятые клектки: {[cell for cell in self.cells]}')


def check_winner(cells):
    winner_cells_1 = [[[str(row), str(coll)] for coll in range(1, 4)] for row in range(1, 4)]
    winner_cells_2 = [[[str(row), str(coll)] for row in range(1, 4)] for coll in range(1, 4)]
    winner_cells_3 = [[str(row), str(coll)] for coll in range(1, 4) for row in range(1, 4) if row == coll]
    winner_cells_4, num = [], 0
    for row in range(1, 4):
        for coll in range(3 - num, 0, -3):
            winner_cells_4.append([str(row), str(coll)])
            num += 1
    winner_cells_1.extend(winner_cells_2)
    winner_cells_1.append(winner_cells_3)
    winner_cells_1.append(winner_cells_4)

    for win_cells in winner_cells_1:
        for cell in win_cells:
            if cell not in cells:
                return False
        else:
            return True


def tic_tac_toe():
    players = [Player(input(f'Введите имя {index} игрока: '), []) for index in range(1, 3)]
    cells = [[str(row), str(coll)] for row in range(1, 4) for coll in range(1, 4)]

    tmp = True
    while tmp == True:
        for player in players:
            if cells == []:
                print('\nНичья!')
                tmp = False
                break

            step = Cell(input(f'\n{player.name}, введите данные клетки через пробел (пример: 1 1): ').split(), player, cells)
            player.cells.append(step.cell)
            player.info()

            if check_winner(player.cells):
                print(f'\n{player.name} победил!')
                tmp = False
                break


tic_tac_toe()
