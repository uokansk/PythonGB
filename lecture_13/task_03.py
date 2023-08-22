def get(text: str = None) -> int:
    while True:
        try:
            num = int(input(text))
            break
        except ValueError as e:
            print(f'your enter error ValueError: {e}\n' 
                  f'try new')
    return num


if __name__ == '__main__':
    number = get('Enter number: ')
    print(f'100 / {number} = {100 / number}')