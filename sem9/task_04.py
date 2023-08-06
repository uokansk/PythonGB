# Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой функции.

from typing import Callable
from functools import wraps


def param_deco(calls_qty: int) -> Callable:
    result = []

    def deco(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(calls_qty):
                result.append((func(*args, **kwargs)))
            return result

        return wrapper

    return deco


@param_deco(5)
def sum_nums(*args):
    return sum(args)


if __name__ == '__main__':
    print(sum_nums(23, 356, 254, 25, 256, 24))
