# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц
# 📌 Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import numpy as np


class Matrix:
    """
    вывода на печать, сравнения, сложения, *умножения матриц
    """
    def __init__(self, matrix):
        self.matrix = matrix

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __gt__(self, other):
        return self.matrix > other.matrix

    def __le__(self, other):
        return self.matrix <= other.matrix

    def __str__(self):
        """
        Преобразуем матрицу в строку для вывода
        """
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        """
        Сложение матриц
        """
        sum_matrix = np.add(self.matrix, other.matrix)
        return sum_matrix

    def __mul__(self, other):
        """
        Умножение матриц
        """
        mul_matrix = np.dot(self.matrix, other.matrix)
        return mul_matrix


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(f'm_1 = \n{m_1}')
print()
print(f'm_2 = \n{m_2}')
print()
sum_m = m_1 + m_2
print(sum_m)
print()
mul_m = m_1 * m_2
print(mul_m)
dif_m = m_1 <= m_2
print(f'm_1 <= m_2 = {m_1 <= m_2}, m_1 == m_2 = {m_1 == m_2}, m_1 > m_2 = {m_1 > m_2},')
