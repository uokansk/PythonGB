# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.
import typing as TextIO


def readline_or_begin(file: TextIO) -> str:
    text = file.readline()
    if text == '':
        file.seek(0)
        text = file.readline()
    return text[:-1]


def read_file():
    with (
        open('task_01_f.txt', encoding='utf-8') as file_num,
        open('names_random.txt', encoding='utf-8') as file_name,
        open('res_file.txt', 'a', encoding='utf-8') as file_res,
    ):
        len_num = len(file_num.readlines())
        len_nam = len(file_name.readlines())
        print(len_num, len_nam)

        for _ in range(max(len_num, len_nam)):
            curr_name = readline_or_begin(file_name)
            # curr_name, _ = curr_name.split('\n')
            curr_number = readline_or_begin(file_num)
            print(curr_number)
            a, b = curr_number.split("|")
            # b, _ = b.split('\n')

            result = int(a) * float(b)
            if result > 0:
                file_res.write(curr_name.upper() + ' ' + str(round(result))+'\n')
            else:
                file_res.write(curr_name.lower() + ' ' + str(abs(result))+'\n')


read_file()
