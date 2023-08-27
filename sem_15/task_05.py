# Задание №5
# 📌 Дорабатываем задачу 4.
# 📌 Добавьте возможность запуска из командной строки.
# 📌 При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# 📌 *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые, т.е не мая, а 5.


from datetime import datetime
import logging
import argparse

logging.basicConfig(filename='task_04.log', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)
WEEK_DAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос',)
MONTHS = ('янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек',)


def parse():
    parser = argparse.ArgumentParser(prog='get_data',
                                     description='Ищем день',
                                     epilog='get_data("3-я среда мая")')

    parser.add_argument('-c', '--count', default=1, help='Какой по счету день недели')
    parser.add_argument('-w', '--week_day', default=datetime.now().weekday(), help='Название дня недели')
    parser.add_argument('-m', '--month', default=datetime.now().month, help='Название месяца')
    args = parser.parse_args()
    return get_data(f'{args.count} {args.week_day} {args.month}')


def get_data(data: str) -> datetime:
    try:
        count, week_day, month = data.split()
    except ValueError:
        logger.error(f'Ошибка ввода двнных {data}')
        return None
    # new_count, _ = count.split('-')
    # new_count = int(new_count)
    # а лучше:
    count = int(count[0])
    week_day = WEEK_DAYS.index(week_day[:3])
    month = MONTHS.index(month[:3]) + 1
    i = 0
    for day in range(1, 32):
        data = datetime(day=day, month=month, year=datetime.now().year)
        if data.weekday() == week_day:
            i += 1
            if i == count:
                return data

    print(count, type(count), week_day, type(week_day), month)


if __name__ == '__main__':
    print(parse())
