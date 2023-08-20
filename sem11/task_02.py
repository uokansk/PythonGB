# 📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# 📌 list-архивы также являются свойствами экземпляра
# Добавьте методы представления экземпляра для программиста и для пользователя.

class Archive:
    _instance = None

    def __init__(self, text, num):
        print('init')
        # print(self.__name__)
        self.text = text
        self.num = num

    def __new__(cls, *args, **kwargs):
        print('new')
        # print(cls.__name__)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nums_archive = []
            cls._instance.text_archive = []
        else:
            cls._instance.nums_archive.append(cls._instance.num)
            cls._instance.text_archive.append(cls._instance.text)

        return cls._instance

    def __str__(self):
        return f'We have text: {self.text} and number {self.num}\n ' \
               f'Archive of text {self.text_archive}\n ' \
               f'Archive of nums {self.nums_archive}'

    def __repr__(self):
        return f'We have text: {self.text} and number: {self.num} '


elem_1 = Archive('text1', 12)
elem_2 = Archive('text2', 1)
elem_3 = Archive('text3', 5)

print(Archive._instance.nums_archive)

print(elem_1)
print(repr(elem_1))
