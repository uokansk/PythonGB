# -*- coding: cp1251 -*-
# ? ���������� ������ 3 � 4. �������� ����� �������, ������� ����� ��������� ������:
# ? �������� ������ (������� �� ������� 4)
# ? ���� � ������� - ������� ������� ��� � id ������������. ��� �������� ������� ������������
# � ��������� ����������� ���������� ����� �������� �� ��������� �������������.
# ���� ������ ������������ ���, ��������� ����������
# �������. � ���� ������������ ����, �������� ��� ������� ��
# ��������� �������������.
# ? ���������� ������������. ���� ������� ������������
# ������, ��� ��� �������, ��������� ���������� ������ �������.

# ������� �6
# ? ����������� ������ ���������� ���, ����� ��� ������ ��������� ���������� �� �������.
# ? ����������� ����������� ������ �� ��������� ���� �������.


import json
from typing import Set

from task_03 import LevelException, AccessException
from task_04 import User


class Project:
    def __init__(self, json_file_path: str):
        self.admin_user = None
        self.json_file_path = json_file_path
        self.users = self.users_from_json()

    def users_from_json(self) -> Set[User]:
        with open(self.json_file_path, 'r', encoding='utf-8') as json_f:
            data = json.load(json_f)
        users = set()
        for user in data:
            users.add(User(user['name'], int(user['user_id']), int(user['access_level'])))
        return users

    def save_users(self):
        with open(self.json_file_path, 'w', encoding='utf-8') as json_f:
            data = [{'name': user.name, 'user_id': user.user_id, 'access_level': user.user_level}
                    for user in self.users]
            json.dump(data, json_f, indent=2, ensure_ascii=False)

    def entrance(self, name: str, user_id: int):
        test_user = User(name, user_id, 0)
        if test_user in self.users:
            self.admin_user = test_user
            for user in self.users:
                if test_user == user:
                    self.admin_user = user
        else:
            raise AccessException(name, user_id)

    def add_user(self, name: str, user_id: int, user_level: int):
        if user_level > self.admin_user.user_level:
            raise LevelException(user_level, self.admin_user)
        new_user = User(name, user_id, user_level)
        self.users.add(new_user)
        self.save_users()


if __name__ == '__main__':
    my_project = Project('task_04_file.json')
    my_project.entrance('Masha', 13)
    my_project.add_user('Anton', 15, 1)
    print(*my_project.users, sep='\n')
