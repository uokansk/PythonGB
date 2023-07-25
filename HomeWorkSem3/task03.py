# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

tings_trip = {'tent': 5,
              'buts': 5,
              'lamp': 3,
              'food': 3,
              'bool': 1,
              'axe': 1,
              'water': 3,
              }
max_weight = 4
possible_items = []
for item, weight in tings_trip.items():
    if weight <= max_weight:
        possible_items.append(item)
        max_weight -= weight
print(possible_items)
