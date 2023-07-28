# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.


len_iter = 101
# for i in range(0, len_iter, 2):
#     if (i % 10 + i // 10) != 8:
#         print(i)
# print(*(i for i in range(0, len_iter, 2) if (i % 10 + i // 10) != 8))

sum_digits = 0
for i in range(0, len_iter, 2):
    sum_digits = 0
    for digit in str(i):
        sum_digits += int(digit)
    if sum_digits != 8:
        print(i, end=' ')

# print(*(i for i in range(0, len_iter, 2) for digit in str(i) sum_digits += int(digit)if (i % 10 + i // 10) != 8))
