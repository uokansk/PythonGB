# ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.
import random

MAX_NUM = 1000
MIN_NUM = -1000


# def fill_file(count_s, name_f):
#     for _ in range(count_s):
#         f = open(name_f, 'a', encoding='utf-8')
#         f.write(str(random.randint(MIN_NUM, MAX_NUM)) + '|' + str(round(random.uniform(MIN_NUM, MAX_NUM), 2)) + "\n")
#         f.close()
    # while count_s > 0:
    #     f = open(name_f, 'a', encoding='utf-8')
    #     f.write(str(random.randint(-1000, 1000)))
    #     f.write('|')
    #     f.write(str(round(random.uniform(-1000, 1000), 2)))
    #     f.write('\n')
    #     f.close()
    #     count_s -= 1
    # return f


#     или
def fill_file(count_s, name_f):
    with open(name_f, 'a', encoding='utf-8') as f:
        for _ in range(count_s):
            f.write(
                str(random.randint(MIN_NUM, MAX_NUM)) + '|' + str(random.uniform(MIN_NUM, MAX_NUM)) + '\n')


count_str = 9
name_file = 'task_01_f.txt'
fill_file(count_str, name_file)
