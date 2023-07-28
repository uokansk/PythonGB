# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

names = ['Tom', 'Maks', 'Bil']
rates = [2000, 3000, 4000]
percents = [10.25, 9.25, 8.25]
my_dict = {}

for name, rate, percent in zip(names, rates, percents):
    my_dict.setdefault(name, rate * percent)
print(my_dict)
print()
print(*((name, rate * percent) for name, rate, percent in zip(names, rates, percents)))
