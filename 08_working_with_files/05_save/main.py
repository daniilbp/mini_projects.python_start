import os

def write(path, info):
    with open(path, 'w') as file:
        file.write(info)
    print('Файл успешно сохранён!')

def read(path):
    with open(path, 'r') as file:
        data = file.read()
    print('\nСодержимое файла:\n' + data)

def do_file(info):
    folders = '/'.join(input('\nКуда хотите сохранить документ? Введите последовательность папок (через пробел):\n').split())
    path = os.path.abspath(os.path.join(os.path.sep, folders))

    if os.path.exists(path) == False:
        print('Из указанных папок пути на диске не существует.')
        new_path = do_file(info)
        return new_path

    name_file = input('\nВведите имя файла: ')
    new_path = os.path.join(path, name_file + '.txt')

    if os.path.exists(new_path):
        choice = input('Вы действительно хотите перезаписать файл? ').lower()
        if choice == 'да':
            write(new_path, info)

    else:
        write(new_path, info)

    return new_path

text = input('Введите строку: ')

need_path = do_file(text)

read(need_path)
