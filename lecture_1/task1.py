"""написание кода согласно стандартам pep-8"""

name = 'Alex'
age = None

a = 5
print(id(a))
a = 'Hello wold!'
print(id(a))
a = 3.14 / 3
print(id(a))

print(name, age, a, 456, 'text')
print(name, age, a, 456, 'text', sep=' (=^.^=) ')
print(name, age, a, 456, 'text', sep=' (=^.^=) ', end='#')
print('Any text')

# res = input('Enter your text: ')
# print('You write ', res)
# константа ADULT
ADULT = 18
age = int(input('Enter your age: '))
# how_old = age - 18
how_old = age - ADULT
print(how_old, "лет назад ты стал совершеннолетним")
