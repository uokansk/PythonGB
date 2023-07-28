def put_money(a, b):
    if b % 50 == 0:
        a += b
    return a


count = 0
money = 100
cash = 51
print(put_money(money, cash))
