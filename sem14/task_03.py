# 📌 Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

from string import ascii_letters
import unittest


def delete_char(text):
    return ("".join(i for i in text if i in ascii_letters + ' ')).lower()


class TestFilterLower(unittest.TestCase):
    def test_return_no_change(self):
        self.assertEqual(delete_char('hello py'), 'hello py', msg='All right')

    def test_return_lower(self):
        self.assertEqual(delete_char('Hello Py'), 'hello py', msg='All right')

    def test_punctuation(self):
        self.assertEqual(delete_char('hello!,. py!'), 'hello py', msg='All right')

    def test_other_char(self):
        self.assertEqual(delete_char('бhello5 pyа'), 'hello py', msg='All right')

    def test_all_mistakes(self):
        self.assertEqual(delete_char('бHe!llo5 Pyа!'), 'hello py', msg='All right')


if __name__ == '__main__':
    # s = 'It15 is true55, I haБ,ve no memoryвава of my accбббident.'
    # print(delete_char(s))
    unittest.main()
