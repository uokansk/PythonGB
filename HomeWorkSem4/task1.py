# Напишите функцию для транспонирования матрицы
# import numpy as np
#
#
# def matrix_trans(mat):
#     trans_matrix = np.transpose(mat)
#     return trans_matrix
#
#
# matrix = np.array([[1, 2], [4, 5], [7, 8]])
# print(matrix_trans(matrix))


def matrix_trans(mat):
    trans_matrix = [[0 for j in range(len(mat))] for i in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            trans_matrix[j][i] = mat[i][j]
    return trans_matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_trans(matrix))

