# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).
from math import sqrt as sq
from random import randint as rnd
from sys import getsizeof as size

print(f'{rnd(1, 8) = }')
# x = [11, 22]
# print(f'{size(x) = }')
# print(f'{sq(25) = }')
