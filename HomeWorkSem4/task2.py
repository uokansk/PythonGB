# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def my_dict(a):
    return a


a = dict(a=1, b=2, c=3)
print(my_dict(a))
