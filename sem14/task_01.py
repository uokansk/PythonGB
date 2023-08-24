# 📌 Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.
# LATIN_ALPHA = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
# LATIN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'
from string import ascii_letters


def delete_char(text):
    # new_text = ''
    # for i in text:
    #     if i in ascii_letters + ' ':
    #         new_text += i
    # return new_text
    return ("".join(i for i in text if i in ascii_letters + ' ')).lower()


if __name__ == '__main__':
    s = 'It15 is true55, I haБ,ve no memoryвава of my accбббident.'
    print(delete_char(s))




