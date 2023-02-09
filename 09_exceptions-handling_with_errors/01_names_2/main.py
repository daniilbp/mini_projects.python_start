with open('people.txt', 'r', encoding='utf-8') as file, open('errors.log', 'w') as file_error:
    count_line, result = 0, 0
    for i_line in file:
        count_line += 1
        try:
            if len(i_line.rstrip()) < 3:
                raise ValueError
            result += len(i_line.rstrip())
        except ValueError as exc:
            print(f'Ошибка: менее трёх символов в строке {count_line}.')
            file_error.write(str(type(exc)) + ' - ' + f'Ошибка: менее трёх символов в строке {count_line}.' + '\n')

print(f'Общее количество символов: {result}.')
