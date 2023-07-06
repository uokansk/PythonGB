# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
# проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч.
from math import sqrt

min_limit = 2
max_limit = 100000
num = None
while True:
    print('Input number behind', min_limit, 'and', max_limit, ': ')
    num = int(input())
    if num < min_limit or num > max_limit:
        print('Not right')
    else:
        i = 2
        while i <= sqrt(num):
            if num % i == 0:
                print("Composite number")
                break
            i += 1
        else:
            print("Prime number")
        break
print(type(num))
