def generator(obj_1, obj_2):

    if isinstance(obj_1, dict) and isinstance(obj_2, dict) == False:
        lst_1 = list(obj_1)
        generator_zip = ((lst_1[i_el], obj_2[i_el]) for i_el in range((len(lst_1) + len(obj_2)) // 2))

    elif isinstance(obj_2, dict) and isinstance(obj_1, dict) == False:
        lst_2 = list(obj_2)
        generator_zip = ((obj_1[i_el], lst_2[i_el]) for i_el in range((len(obj_1) + len(lst_2)) // 2))

    elif isinstance(obj_1, dict) and isinstance(obj_2, dict):
        lst_1, lst_2 = list(obj_1), list(obj_2)
        generator_zip = ((lst_1[i_el], lst_2[i_el]) for i_el in range((len(lst_1) + len(lst_2)) // 2))

    else:
        generator_zip = ((obj_1[el], obj_2[el]) for el in range((len(obj_1) + len(obj_2)) // 2))

    print(f'\nРезультат:\n{generator_zip}')

    for tuple_el in generator_zip:
        print(tuple_el)

input_1 = 'abcd'
input_2 = {1: 123, 2: 456, 3: 789, 4: 321, 5: 458}

print('Строка:', input_1)
print('Кортеж чисел:', input_2)

generator(input_1, input_2)

# v2
# + if-ы для всех т.д.
# generator_zip = ((input_1[el], input_2[el]) for el in range((len(input_1) + len(input_2)) // 2))
#
# print(f'\nРезультат:\n{generator_zip}')
# for tuple_el in generator_zip:
#     print(tuple_el)
