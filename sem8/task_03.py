# -*- coding: cp1251 -*-
# ? �������� �������, ������� � ����������� ����� ����������� ���, ������ ������������� � �������
# ������� (�� 1 �� 7).
# ? ����� ������� ����� ���������� ����� ���������� � JSON ����.
# ? ������������ ������������ �� ������ �������.
# ? ������������� ������������ ��������� ������ ��� �����.
# ? ���������, ��� ��� �������������� ��������� ���������� �� ������ �������.
# ? ��� ����������� ������� ��� ���������� � ���� ������ ������ �����������.
import json
import os


def add_data_to_json(json_file):
    users_id = set()
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as data_file:
            data = json.load(data_file)
            for user in data.values():
                users_id.update(user.keys())
    else:
        data = {str(access_level): dict() for access_level in range(1, 8)}

    while True:
        name = input('Enter name: ')
        if not name:
            break
        id = input('Enter ID: ')
        access_level = input('Enter level access: ')
        if id in users_id:
            continue
        data[access_level][id] = name
        with open(json_file, 'w', encoding='utf-8') as data_file:
            json.dump(data, data_file, indent=2, ensure_ascii=False)


add_data_to_json('task_03_file.json')
