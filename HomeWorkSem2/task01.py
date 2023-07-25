# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

number = int(input('Enter a number: '))
hex_number = ''
check_number = hex(number)
while number != 0:
    var = number % 16
    if var == 10:
        hex_number = 'A' + hex_number
    elif var == 11:
        hex_number = 'B' + hex_number
    elif var == 12:
        hex_number = 'C' + hex_number
    elif var == 13:
        hex_number = 'D' + hex_number
    elif var == 14:
        hex_number = 'E' + hex_number
    elif var == 15:
        hex_number = 'F' + hex_number
    else:
        hex_number = str(var) + hex_number
    number = number // 16

print('0X' + hex_number, ' examination -', check_number.upper())
