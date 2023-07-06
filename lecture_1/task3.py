pwd = 'text'
res = input('Input password: ')
if res == pwd:
    print('Access is allowed :)')
    my_math = int(input('2 + 2 = '))
    if 2 + 2 == my_math:
        print('You are in the normal world!')
    else:
        print('But be careful!')
else:
    print('Access is denied :(')
print('Work completed')
