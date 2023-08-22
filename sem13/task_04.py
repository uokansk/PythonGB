# -*- coding: cp1251 -*-
# ? Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# ? Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# ? Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.
import json

from typing import Set


class User:
    def __init__(self, name: str, user_id: int, user_level: int):
        self.name = name
        self.user_id = user_id
        self.user_level = user_level

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

    def __hash__(self):
        return hash((self.name, self.user_id))

    def __str__(self):
        return f'name: {self.name}, id: {self.user_id}, level: {self.user_level}'


def users_from_json(json_file_path: str) -> Set[User]:
    with open(json_file_path, 'r', encoding='utf-8') as json_f:
        data = json.load(json_f)
    user_set = set()
    for user in data:
        user_set.add(User(user['name'], int(user['user_id']), int(user['access_level'])))
    return user_set


if __name__ == '__main__':
    print(*users_from_json('task_04_file.json'), sep='\n')
