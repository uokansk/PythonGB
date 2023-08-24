# 📌 Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
from string import ascii_letters
import pytest


def delete_char(text):
    return ("".join(i for i in text if i in ascii_letters + ' ')).lower()


def test_return_no_change():
    assert delete_char('hello py') == 'hello py', 'Логика покинула чат'


def test_return_lower():
    assert delete_char('Hello Py') == 'hello py'


def test_punctuation():
    assert delete_char('hello!,. py!') == 'hello py'


def test_other_char():
    assert delete_char('бhello5 pyа') == 'hello py'


def test_all_mistakes():
    assert delete_char('бHe!llo5 Pyа!') == 'hello py'


# if __name__ == '__main__':
#     s = 'It15 is true55, I haБ,ve no memoryвава of my accбббident.'
#     print(delete_char(s))

if __name__ == '__main__':
    pytest.main(['-vv'])
