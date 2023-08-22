# -*- coding: cp1251 -*-
# ? �������� ������� ������ get ��� �������.
# ? ������ ������ ������� ������� ��������� ���� �
# �������� �� ���������.
# ? ��� ��������� � ��������������� ����� ������� ������
# ���������� ��������� ��������.
# ? ���������� ������ ����� ��������� ����������.

def analog_get(dct: dict, key: str, default: int | float = None) -> int | float | None:
    result = default
    try:
        result = dct[key]
    except KeyError as e:
        pass
    return result


if __name__ == '__main__':
    my_dict = {'a': 56, 'b': 57}
    print(analog_get(my_dict, 'a', 0))
    print(analog_get(my_dict, 'c', 444))
