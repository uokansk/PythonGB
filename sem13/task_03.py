# -*- coding: cp1251 -*-
# �������� ����� � ������� ����������� � �������� ������-����������:
# ? ������ ������,
# ? ������ �������.

# ������� �6
# ? ����������� ������ ���������� ���, ����� ��� ������ ��������� ���������� �� �������.
# ? ����������� ����������� ������ �� ��������� ���� �������.
from task_04 import User


class MyException(Exception):
    pass


class LevelException(MyException):
    def __init__(self, level: int, user: User):
        self.level = level
        self.user = user

    def __str__(self):
        return f'������ �������� ������������ � ������� {self.level}. ' \
               f'D� ����� ��� {self.user} � ������� {self.user.user_level}'


class AccessException(MyException):
    def __init__(self, name: str, user_id: int):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f'�������� � �������. ������������ � ������ {self.name}. ' \
               f'� ID = {self.user_id} �� ������'
