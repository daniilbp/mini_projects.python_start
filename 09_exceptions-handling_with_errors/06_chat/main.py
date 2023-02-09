def action(chat_name, num, name):
    if num == 1:
        with open(chat_name, 'r', encoding='utf-8') as file:
            data = file.read()
            print(data)
    elif num == 2:
        with open(chat_name, 'a') as file:
            user_text = input('\nВведите текст: ')
            file.write(name + ':   ' + user_text + '\n')


def writer(name_chat):
    user_name = input('Введите имя пользователя: ')
    while user_name != 'stop':
        try:
            choice = int(input('\nВыберите одно из действий:\n'
                                '1. Посмотреть текущий текст чата.\n'
                                '2. Отправить сообщение (затем вводит сообщение).\n'
                               'Выберите 1 или 2: '))
            if choice < 1 or choice > 2:
                raise ValueError

            action(name_chat, choice, user_name)

            user_name = input('\nВведите имя пользователя: ')

        except ValueError:
            print('\nВведен некорректный номер действия.')
            user_name = input('\nВведите имя пользователя: ')


writer('chat.txt')
