# -*- coding: cp1251 -*-

def hundred_div_num(text: str = None) -> tuple[int, float]:
    while True:
        try:
            num = int(input(text))
            div = 100 / num
            break
        except ValueError as e:
            print(f'��� ���� ����� � ������ ValueError: {e}\n'
                  f'���������� �����')
        except ZeroDivisionError as e:
            div = float('inf')
            break
    return num, div


if __name__ == '__main__':
    n, d = hundred_div_num('������� ����� ��������: ')
    print(f'��������� ��������: "100 / {n} = {d}"')
