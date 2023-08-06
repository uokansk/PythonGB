# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
import random
from typing import Callable


def guess_number(seсret_num: int, attempt: int) -> Callable[[], None]:
    def giv_number():
        for i in range(1, attempt + 1):
            answer = int(input(f'You have {i} tries, enter number: '))
            if seсret_num > answer:
                print(f'enter more {answer}')
            elif seсret_num < answer:
                print(f'enter less {answer}')
            else:
                print('you win!')
                break
            # return (f'game over, hidden number is {a}')

    return giv_number


if __name__ == '__main__':
    start_number = 1
    stop_number = 100
    hidden_number = random.randint(start_number, stop_number)
    number_attempts = 7
    game = (guess_number(hidden_number, number_attempts))
    game()
