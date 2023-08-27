# Задание №1
# 📌 Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# 📌 Например отлавливаем ошибку деления на ноль.
import logging

logging.basicConfig(filename='division.log.', filemode='w', encoding='utf-8', level=logging.ERROR)


def division(a: int, b: int) -> float:
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error(f' {a}/{b}, это деление на ноль! \n {e}')
        result = float('inf')
    return result


if __name__ == '__main__':
    print(division(10, 2))
    print(division(10, 0))
