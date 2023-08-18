# 📌 Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть # методы birthday для увеличения возраста на год, full_name для
# вывода полного ФИО и т.п. на ваш выбор.
# 📌 Убедитесь, # что свойство возраст недоступно для прямого изменения, но есть возможность
# получить текущий возраст.
from enum import Enum


class Gender(Enum):
    male = 'male'
    female = 'female'


class Person:
    def __init__(self, family: str, name: str, surname: str, age: int, gender: Gender):
        self.family = family
        self.name = name
        self.surname = surname
        self._age = age
        self.gender = gender

    def full_name(self):
        # return self.family + ' ' + self.name + ' ' + self.surname
        return f'{self.family} {self.name} {self.surname}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


if __name__ == "__main__":
    p1 = Person('Sawyer', 'Tom', 'Ivanovich', 27, Gender.male)
    print(p1.full_name())
    print(p1.get_age())
    p1.birthday()
    print(p1.get_age())
    print(p1.gender)

