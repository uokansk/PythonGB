# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# 📌 Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
import csv
import json
import random


def quadratic_equation(file_name):
    results = []

    def read_data_scv():
        with open(file_name, 'r', newline='') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                a, b, c = line
                a, b, c = int(a), int(b), int(c)
                if a == 0:
                    continue
                discriminant = pow(b, 2) - 4 * a * c
                if discriminant < 0:
                    answer = 'Not root'
                elif discriminant == 0:
                    x = -b / (2 * a)
                    answer = x
                else:
                    x1 = (-b + pow(discriminant, 0.5)) / (2 * a)
                    x2 = (-b - pow(discriminant, 0.5)) / (2 * a)
                    answer = x1, x2

                results.append({"a, b, c": line, "root": answer})
                with open("output.json", "w") as json_file:
                    json.dump(results, json_file, indent=2)

    return read_data_scv()


def generate_csv_file(file_name):
    count_num = 3
    count_str = random.randint(100, 1000)
    with open(file_name, "w", newline="") as file:
        for _ in range(count_str):
            writer = csv.writer(file)
            writer.writerow([random.randint(-10, 10) for _ in range(count_num)])


if __name__ == '__main__':
    name_file = 'number.csv'
    generate_csv_file(name_file)
    quadratic_equation(name_file)