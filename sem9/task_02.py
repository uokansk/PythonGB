# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-
# угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.

import random
from functools import wraps
from typing import Callable


def guess_number(func: Callable) -> Callable[[int, int], None]:
    start_number = 1
    stop_number = 100
    stop_number_try = 10

    @wraps(func)
    def giv_number(secret_num: int, count_tries: int, *args, **kwargs):
        if not start_number <= secret_num <= stop_number:
            secret_num = random.randint(start_number, stop_number)
        if not start_number <= count_tries <= stop_number_try:
            count_tries = random.randint(start_number, stop_number_try)

        return func(secret_num, count_tries, *args, **kwargs)

    return giv_number


@guess_number
def func_mun(secret_num: int, count_tries: int):
    for i in range(1, count_tries + 1):
        answer = int(input(f'You have {count_tries + 1 - i} tries, enter number: '))
        if secret_num > answer:
            print(f'enter more {answer}')
        elif secret_num < answer:
            print(f'enter less {answer}')
        else:
            print('you win!'.upper())
            return


if __name__ == '__main__':
    # start_number = 1
    # stop_number = 100
    # stop_number_try = 10
    # hidden_number = random.randint(start_number, stop_number)
    # number_attempts = 9
    func_mun(55, 9)
