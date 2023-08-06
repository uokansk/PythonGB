# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
from typing import Callable


def guess_number(hidden_number: int, number_attempts: int) -> Callable[[], None]:
    def number_funk():
        for i in range(1, number_attempts + 1):
            answer = int(input(f'You have {i} tries, enter number: '))
            if hidden_number == answer:
                print('You win!')
                break
            elif hidden_number > answer:
                print('enter more')
            elif hidden_number < answer:
                print('enter less')

    return number_funk


if __name__ == '__main__':
    game = (guess_number(50, 5))
    game()
