# Задание №4
# 📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.
from datetime import datetime
import logging

logging.basicConfig(filename='task_04.log', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)
WEEK_DAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос',)
MONTHS = ('янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек',)


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
    print(get_data('5-я суббота май'))
