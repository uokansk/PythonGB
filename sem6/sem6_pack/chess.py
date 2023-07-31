# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
# ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
__all__ = ['enter_date', 'plant_queen']

CELLS = 8
def plant_queen(x, y, cells):
    correct = True
    for i in range(cells):
        for j in range(i + 1, cells):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
                return correct
    return correct


def enter_date(b):
    x = []
    y = []
    for i in range(b):
        new_x, new_y = [int(s) for s in input('введи координату ферзя: ').split()]
        x.append(new_x)
        y.append(new_y)
    return plant_queen(x, y, b)


if __name__ == '__main__':
    print(enter_date(CELLS))
