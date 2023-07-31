# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv

__all__ = ['check_year']


def check_year(data: str) -> bool:
    day, mon, year = map(int, data.split('.'))
    if not (1 <= day <= 31 and 1 <= mon <= 12 and 1 <= year <= 9999):
        return False
    if mon in (4, 6, 9, 11) and day > 30:
        return False
    if mon == 2 and leap_year(year) and day > 29:
        return False
    if mon == 2 and not leap_year(year) and day > 28:
        return False

    return True


def leap_year(year: str):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


if __name__ == '__main__':
    name, *param = argv
    print(check_year('29.02.2000'))
