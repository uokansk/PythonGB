# a, b, c = input('Введите 3 числа через пробел: ').split()
# print(c, b, a)

# data = ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1', 'posts', '']
# url = '/'.join(data)
# print(url)


# text = 'Привет, мир!'
# print(text.find(' '))
# print(text.title())
# print(text.split())
# print(f'{text = :>25}')

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# my_dict['ten'] = 10
# my_dict['five'] = 5
# print(my_dict)

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.setdefault('ten', 555))
# print(my_dict.values())
# print(my_dict.pop('one'))
# my_dict['one'] = my_dict['four']
# print(my_dict)

# my_set = frozenset({3, 4, 1, 2, 5, 6, 1, 7, 2, 7})
# print(len(my_set))
# print(my_set - {1, 2, 3})
# print(my_set.union({2, 4, 6, 8}))
# print(my_set & {2, 4, 6, 8})
# print(my_set.discard(10))

# my_set = {}
# my_set.add(9)
# print(my_set)

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.values())
for value in my_dict.values():
    print(value)
