user_str_1 = input('Первая строка: ')
user_str_2 = input('Вторая строка: ')

for i_num in range(1, len(user_str_1) - 1):
    new_user_str_1 = ''.join([user_str_1[(new_i_num + i_num) % len(user_str_1)] for new_i_num in range(len(user_str_1))])
    if new_user_str_1 == user_str_2:
        print('\nПервая строка получается из второй со сдвигом', len(user_str_1) - i_num, '.')
        break
else:
    print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')