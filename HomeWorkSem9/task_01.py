# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# 📌 Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
import csv
import functools
import random


def quadratic_equation(line):
    a, b, c = map(int, line)
    if a == 0:
        print(f'None: a = 0')
    discriminant = pow(b, 2) - 4 * a * c
    if discriminant < 0:
        print(f'Not root')
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f'one root {x}')
    else:
        x1 = (-b + pow(discriminant, 0.5)) / (2 * a)
        x2 = (-b - pow(discriminant, 0.5)) / (2 * a)
        answer = x1, x2
        print(f'two root {answer}')


def generate_csv_file(file_name):
    count_num = 3
    # count_str = random.randint(100, 1000)
    count_str = 5
    with open(file_name, "w", newline="") as file:
        for _ in range(count_str):
            writer = csv.writer(file)
            writer.writerow([random.randint(-10, 10) for _ in range(count_num)])


def read_data_scv(file_name):
    with open(file_name, 'r', newline='') as f:
        csv_file = csv.reader(f)
        for line in csv_file:
            return line





name_file = "number.csv"
generate_csv_file(name_file)
print(quadratic_equation(read_data_scv(name_file)))
