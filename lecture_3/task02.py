# Метод append
# Для добавления нового элемента в конец списка используется метод append. Метод
# принимает один аргумент — объект который будет добавлен в конец динамически
# увеличенного списка.
a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
my_list.append(a)
print(my_list)
my_list.append(b)

print(my_list)
my_list.append(c)
print(my_list)
my_list.append(my_list)  # это нельзя делать
print(my_list)
