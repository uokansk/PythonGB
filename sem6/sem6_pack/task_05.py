# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.


def puzzle(puzzle_text: str, answers: list[str], trials: int):
    print(puzzle_text, answers)
    try_count = 1
    while trials > 0:
        current_try = input(f'Осталось попыток: {trials}. Ваш ответ: ')
        if current_try in answers:
            return try_count
        try_count += 1
        trials -= 1
    else:
        return trials


def storage(trial_amount: int = 3):
    puzzle_dict = {'Puzzle?': ['yes', 'sure'],
                   'still_puzzle?': ['no', 'maybe'],
                   'beetle?': ['bug', 'dor'],
                   }
    for puz, ans in puzzle_dict.items():
        puzzle(puz, ans, trial_amount)


if __name__ == '__main__':
    print(storage())
