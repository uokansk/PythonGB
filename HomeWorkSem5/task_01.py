# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def file_way(all_way):
    way, type_file = all_way.split('.')
    *_, name_file = way.split('\\')
    way_file, *_ = way.split(name_file)
    a = (way_file, name_file, type_file)
    return a


file = 'D:\обучение\python\л3\Лекция_3_Коллекции.pdf'
print(file_way(file))
