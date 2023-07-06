year = int(input('Input year in format yyyy: '))
if year % 4 != 0:
    print('normal')
elif year % 100 == 0:
    if year % 400 == 0:
        print('Leap year')
    else:
        print('normal')
else:
    print('Leap year')
