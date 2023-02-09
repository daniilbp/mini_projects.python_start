menu_str_input = 'утиное филе;фланк-стейк;банановый пирог;плов'

# menu_list = menu_str_input.split(';')
#
# menu_str_output = ', '.join(menu_list)

menu_str_output = menu_str_input.replace(';', ', ')

print('Доступное меню:', menu_str_input)
print('\nНа данный момент в меню есть:', menu_str_output)
