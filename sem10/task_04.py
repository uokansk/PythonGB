# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
from random import randint

from task_03 import Person, Gender


class Employee(Person):
    MAX_LEVEL = 7
    MIN_ID = 100000
    MAX_ID = 999999

    def __init__(self, family: str, name: str, surname: str, age: int, gender: Gender, emp_id: int):
        super().__init__(family, name, surname, age, gender)
        if self.MIN_ID < emp_id <= self.MAX_ID:
            self.emp_id = emp_id
        else:
            self.emp_id = randint(self.MIN_ID, self.MAX_ID)

        self.level = self.get_level()

    def get_level(self):
        nums_of_id = sum(int(n) for n in str(self.emp_id))
        return nums_of_id % self.MAX_LEVEL


emp_1 = Employee('Sawyer', 'Tom', 'Ivanovich', 27, Gender.male, 777777)
print(emp_1.get_level())
print(hash(emp_1))

emp_2 = Employee('Sawyer', 'Tom', 'Ivanovich', 27, Gender.male, 777777)
print(emp_2.get_level())
print(hash(emp_2))
