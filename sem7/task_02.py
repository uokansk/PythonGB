# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
import random
import string


def name_generation(name_len):
    with open('names_random.txt', 'a', encoding='utf-8') as f:
        text = ''.join(random.choices(string.ascii_lowercase, k=name_len)).title()
        f.write(text + '\n')


min_num = 4
max_mun = 7
len_name = random.randint(min_num, max_mun)
name_generation(len_name)


# import random

# #согласные
# consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q',
#         'R', 'S', 'T', 'V', 'W', 'X', 'Z']
#
# #гласные
# vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
#
#
# def id_generator(size=5):
#   flag, word = True, ''
#   for i in range(size):
#     flag, word = not flag, word + random.choice(consonants) if flag else word + random.choice(vowels)
#   print(word)
#
# id_generator()
