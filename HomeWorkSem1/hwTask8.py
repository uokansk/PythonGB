# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов
SPACE = ' '
STAR = '*'
rows = int(input('Input count rows: '))
spaces = rows - 1
stars = 1
for i in range(rows):
    print((SPACE * spaces) + (STAR * stars) + (SPACE * spaces))
    stars += 2
    spaces -= 1
