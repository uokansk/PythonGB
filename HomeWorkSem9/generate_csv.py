import csv
import random


def generate_csv_file(file_name):
    count_num = 3
    # count_str = random.randint(100, 1000)
    count_str = 5
    with open(file_name, "w", newline="") as file:
        for _ in range(count_str):
            writer = csv.writer(file)
            writer.writerow([random.randint(-10, 10) for _ in range(count_num)])


name_file = "number.csv"
generate_csv_file(name_file)
