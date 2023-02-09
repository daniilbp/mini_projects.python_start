def init_action(info):
    result = None
    if info[1] == '+':
        result = int(info[0]) + int(info[2])
    elif info[1] == '-':
        result = int(info[0]) - int(info[2])
    elif info[1] == '*':
        result = int(info[0]) * int(info[2])
    elif info[1] == '/':
        result = int(info[0]) / int(info[2])
    elif info[1] == '//':
        result = int(info[0]) // int(info[2])
    elif info[1] == '%':
        result = int(info[0]) % int(info[2])

    return result


with open('calc.txt', 'r') as file:
    sum_res = 0
    for line in file:
        lst_line = line.split()
        try:
            res = init_action(lst_line)
            if not res:
                raise ValueError
            sum_res += res
        except ValueError:
            print(f'Обнаружена ошибка в строке: {line.rstrip()}', end='   ')
            choice = input('Хотите исправить? ').lower()
            if choice == 'да':
                new_line = input('Введите исправленную строку: ').split()
                res = init_action(new_line)
                sum_res += res

print('\nСумма результатов:', sum_res)
