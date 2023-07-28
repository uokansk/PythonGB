# ✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт» без перехода на новую строку.

print('Таблица умножения')
print()
for i in range(2, 10, 4):
    for j in range(2, 11):
        for k in range(i, i + 4):
            if k != i + 3:
                print(f'{k:>2} x {j:>2} = {k * j:>2}\t')
            elif j != 10:
                print(f'{k:>2} x {j:>2} = {k * j:>2}\n')
            else:
                print(f'{k:>2} x {j:>2} = {k * j:>2}\n\n')

# milt_tab = (f'\t{k:>2} x {j:>2} = {k * j:>2}\t' if k != i + 4 - 1 else
#             f'{k:>2} x {j:>2} = {k * j:>2}\n' if j != 10 else
#             f'{k:>2} x {j:>2} = {k * j:>2}\n\n'
#             for i in range(2, 10, 4)
#             for j in range(2, 11)
#             for k in range(i, i + 4))
# print(*milt_tab, end='  ')

# for i in range(2, 10):
#     for j in range(2, 10):
#         print(f'{j} x {i} = {i * j:>2}\t', end='  ')
#     print()

# tab = (f'\t{j} x {i} = {i * j:>2}\n' for j in range(2, 10) for i in range(2, 10))
# print(*tab)
