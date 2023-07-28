# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым,
# если делится нацело только на единицу и на себя».

def simple_num(n):
    for i in range(2, n + 1):
        is_prime: bool = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i


for k in (simple_num(97)):
    print(k, end=' ')
