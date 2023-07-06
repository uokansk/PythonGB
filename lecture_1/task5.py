year = int(input('Input year in format yyyy: '))
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print('Normal year')
else:
    print('Leap year')
