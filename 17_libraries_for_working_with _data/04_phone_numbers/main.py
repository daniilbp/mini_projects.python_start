import re


count = 0


def check_phone_num(number: str) -> None:
    num_dct = {1: 'первый', 2: 'второй', 3: 'третий'}
    global count
    count += 1

    if re.findall(r'[89]\d{9}', number):
        print(num_dct[count], 'номер: всё в порядке')
    else:
        print(num_dct[count], 'номер: не подходит')


telephone_list = ['9999999999', '999999-999', '99999x9999']

for num in telephone_list:
    check_phone_num(num)
