# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fibonacci(n):
    fib1 = fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib2


print(1, 1, end=' ')
for k in (fibonacci(10)):
    print(k, end=' ')

