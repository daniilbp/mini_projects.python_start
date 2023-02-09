def is_prime(num):
    result = False
    if num > 1:
        result = True
        for devider in range(2, num):
            if num % devider == 0:
                result = False
                break

    return result

def crypto(input_info):

    return [el if isinstance(input_info, (str, list, tuple, set)) else '{0}: {1}'.format(el, input_info[el])
            for i_el, el in enumerate(input_info) if is_prime(i_el)]

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(crypto({1: 123, 2: 456, 3: 789, 4: 321}))
# print(crypto('О Дивный Новый мир!'))

# 'О Дивный Новый мир!'
# [100, 200, 300, 'буква', 0, 2, 'а']
# {1: 123, 2: 456, 3: 789, 4: 321}
# (100, 200, 300, 'буква', 0, 2, 'а')
# {100, 200, 300, 'буква', 0, 2, 'а'}