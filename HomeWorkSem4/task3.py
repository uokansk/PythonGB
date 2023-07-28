# Напишите программу банкомат. Начальная сумма равна нулю Допустимые действия: пополнить, снять, выйти Сумма
# пополнения и снятия кратны 50 у.е. Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3% Нельзя снять больше, чем на счёте При
# превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной Любое действие
# выводит сумму денег Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления
# и снятия средств в список.


def put_money(a, b):
    if cash % 50 == 0:
        a += b
    return a


def withdraw_money(money, cash):
    if cash % 50 == 0:
        if min_percent < cash * percent < max_percent:
            cash *= percent
            print(f'Процент за снятие {percent}')
            if cash < money:
                money -= cash
        if min_percent > cash * percent:
            cash += min_percent
            print(f'Процент за снятие {min_percent}')
            if cash < money:
                money -= cash
        if cash * percent > max_percent:
            cash += max_percent
            print(f'Процент за снятие {max_percent}')
            if cash < money:
                money -= cash
    return money


operation = 0
cash = 0
count = 0
percent_deposit = 1.03
percent = 1.015
min_percent = 30
max_percent = 600
while True:
    if count == 3:
        file = open("balance.txt", "r")
        money = float(file.readline())
        money *= percent_deposit
        file = open("balance.txt", "w")
        file.write(str(money))
        count = 0
        file.close()
    file = open("balance.txt", "r")
    money = float(file.readline())
    print(f'На вашем счету {money:.2f}')
    operation = input('1 - положить деньги, 2 - снять деньги, 3 - завершить операцию: ')
    file.close()
    if operation == '1':
        file = open("balance.txt", "r")
        money = float(file.readline())
        cash = int(input('Введите сумму кратную 50: '))
        money = put_money(money, cash)
        file = open("balance.txt", "w")
        file.write(str(money))
        file.close()
        count += 1

    if operation == '2':
        cash = int(input('Введите сумму кратную 50: '))
        file = open("balance.txt", "r")
        money = float(file.readline())
        file.close()
        money = withdraw_money(money, cash)
        file = open("balance.txt", "w")
        file.write(str(money))
        file.close()
        count += 1

    if operation == '3':
        print('Приходите ещё!')
        file.close()
        break
