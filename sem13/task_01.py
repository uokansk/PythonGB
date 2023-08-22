# -*- coding: cp1251 -*-
# ? Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# ? Обрабатывайте не числовые данные как исключения.

def get(text: str = None) -> float:
    while True:
        try:
            num = float(input(text))
            break
        except ValueError as e:
            print(f'your enter error ValueError: {e}\n try new')
    return num


if __name__ == '__main__':
    number = get('Enter number: ')
    print(f'All right, your enter {number}')
