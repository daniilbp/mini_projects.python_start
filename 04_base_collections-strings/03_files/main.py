name_file = input('Название файла: ')

special_symbols = '@№$%^&\*()'

if name_file[0] in special_symbols:
    print('\nОшибка: название начинается на один из специальных символов.')

elif not name_file.endswith(('.txt', '.docx')):
    print('\nОшибка: неверное расширение файла. Ожидалось .txt или .docx.')

else:
    print('\nФайл назван верно.')
