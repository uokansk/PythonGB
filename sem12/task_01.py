# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
from collections import deque
import json


class Factorial:
    def __init__(self, k):
        self._history = deque(maxlen=k)

    def __call__(self, number):
        mul_num = 1
        for i in range(2, number + 1):
            mul_num *= i
        self._history.append({number: mul_num})
        return mul_num

    def show_history(self):
        return self._history

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        data = {}
        while self._history:
            data.update(self._history.popleft())
        with open('task_02.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)
        return


if __name__ == '__main__':
    fact_1 = Factorial(5)
    with fact_1 as f:
        print(f(10))
        print(f(15))
        print(f(20))
        print(f.show_history())
