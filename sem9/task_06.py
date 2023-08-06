# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.


from task_02 import guess_number as validate
from task_03 import add_param_to_json
from task_04 import param_deco as trials


@trials(3)
@validate
@add_param_to_json
def func_mun(secret_num: int, count_tries: int):
    for i in range(1, count_tries + 1):
        answer = int(input(f'You have {count_tries + 1 - i} tries, enter number: '))
        if secret_num > answer:
            print(f'enter more {answer}')
        elif secret_num < answer:
            print(f'enter less {answer}')
        else:
            print('you win!'.upper())
            return


if __name__ == '__main__':
    # start_number = 1
    # stop_number = 100
    # stop_number_try = 10
    # hidden_number = random.randint(start_number, stop_number)
    # number_attempts = 3
    func_mun(55, 3)
    print(f'{func_mun.__name__ =}')
