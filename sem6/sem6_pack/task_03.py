# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
from random import randint as rnd
from sys import argv

__all__ = ['get_random_num']

START = 0
STOP = 100
AMOUNT = 5


def get_random_num(start: int = START, stop: int = STOP, count: int = AMOUNT):
    flag = False
    num = rnd(start, stop)
    print(num)
    while count > 0:
        num_user = int(input('enter number: '))
        if num < num_user:
            print('enter less ')
            count -= 1
        elif num > num_user:
            print('enter more ')
            count -= 1
        elif num == num_user:
            print('you are win')
            flag = True
            break
    return flag


if __name__ == '__main__':
    name, *param = argv
    print(get_random_num(*(int(elem) for elem in param)))
