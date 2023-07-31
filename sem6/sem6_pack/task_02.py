# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
from random import randint as rnd

START = 0
STOP = 100
AMOUNT = 5


def get_random_num(start: int, stop: int, count: int):
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
    # data = input('enter Start range and Stop range: ')
    # start, stop = map(int, data.split())
    res = get_random_num(START, STOP, AMOUNT)
    print(res)
