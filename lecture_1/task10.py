min_limit = 0
max_limit = 10
while True:
    print('Input number behind', min_limit, 'and', max_limit, ': ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Not right')
    else:
        break
print('You input', num)
