def init_error(info):
    result = None
    try:
        if len(info) != 3:
            raise IndexError
        elif not lst_line[0].isalpha():
            raise NameError
        elif '@' not in lst_line[1] and '.' not in lst_line[1]:
            raise SyntaxError
        elif int(lst_line[2]) < 10 or int(lst_line[2]) > 99:
            raise ValueError
    except ValueError:
        result = 'Поле «Возраст» НЕ является числом от 10 до 99'
    except SyntaxError:
        result = 'Поле «Имейл» НЕ содержит @ и . (точку)'
    except NameError:
        result = 'Поле «Имя» содержит НЕ только буквы'
    except IndexError:
        result = 'НЕ присутствуют все три поля'

    return result


with open('registrations.txt', 'r', encoding='utf-8') as file, open('registrations_good.log', 'w') as good_file, open('registrations_bad.log', 'w') as bad_file:
    for line in file:
        lst_line = line.split()
        info_error = init_error(lst_line)
        if info_error:
            bad_file.write(line.rstrip() + '        ' + info_error + '\n')
        else:
            good_file.write(line)
