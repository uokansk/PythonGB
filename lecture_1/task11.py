min_limit = 0
max_limit = 10
count = 3
LIMIT = 4
num = None

while count > 0:
    print('Attempt', LIMIT - count)
    count -= 1
    print('Input number behind', min_limit, 'and', max_limit, ': ')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Not right.')
    else:
        break

else:
    print('All attempts ended.')
    quit()

print('You input', num)
