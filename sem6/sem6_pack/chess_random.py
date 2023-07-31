__all__ = ['enter_date', 'plant_queen']

from random import randint as rnd

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
        new_x = random_pear()
        new_y = random_pear()
        x.append(new_x)
        y.append(new_y)
    print(x, y)


def random_pear():
    num1 = rnd(1, 8)
    return num1


if __name__ == '__main__':
    print(enter_date(CELLS))