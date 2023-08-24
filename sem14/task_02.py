# 📌 Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from string import ascii_letters


def delete_char(text: str) -> str:
    """
    >>> delete_char('hello py')
    'hello py'
    >>> delete_char('HeLLo Py')
    'hello py'
    >>> delete_char('hello! py,.')
    'hello py'
    >>> delete_char('hel4lo приветpy')
    'hello py'
    >>> delete_char('HeLLo! приветPyб,.')
    'hello py'
    """
    return ("".join(i for i in text if i in ascii_letters + ' ')).lower()


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
