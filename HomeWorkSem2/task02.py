# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна
# возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

a = input('Enter a number "A" ')
b = input('Enter a number "B" ')
a = a.split('/')
b = b.split('/')

if int(a[1]) == int(b[1]):
    sum_a_b = str(int(a[0]) + int(b[0])) + '/' + str(a[1])
else:
    sum_a_b = str(int(a[0]) * int(b[1]) + int(b[0]) * int(a[1])) + '/' + str(int(a[1]) * int(b[1]))
product_a_b = str(int(a[0]) * int(b[0])) + '/' + str(int(a[1]) * int(b[1]))

f1 = fractions.Fraction(int(a[0]), int(a[1]))
print(f1)
f2 = fractions.Fraction(int(b[0]), int(b[1]))
print(f2)

print(sum_a_b, ' examination -', f1 + f2)
print(product_a_b, ' examination -', f1 * f2)
