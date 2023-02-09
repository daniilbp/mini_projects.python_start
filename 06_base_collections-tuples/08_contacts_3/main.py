def find_contact(telephone_book):

    name = input('Введите фамилию для поиска: ')

    for key in telephone_book:
        if (len(name) <= len(key[1]) and key[1].startswith(name)) or \
                    (len(name) > len(key[1]) and key[1].startswith(name[:len(name) - 1])):
            print(key[0], key[1], telephone_book[key], end='\n\n')


def add_contact(telephone_book):

    user_name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())

    if (user_name[0], user_name[1]) in telephone_book:
        print('Такой человек уже есть в контактах.')

    else:
        user_number = int(input('Введите номер телефона: '))
        telephone_book.update({(user_name[0], user_name[1]): user_number})

    print('Текущий словарь контактов: ', telephone_book, end='\n\n')
    return telephone_book


def choice():

    telephone_book = {}

    while True:
        action = int(input('Введите номер действия:\n1. Добавить контакт\n2. Найти человека\n'))
        if action == 1:
            telephone_book = add_contact(telephone_book)
        elif action == 2:
            find_contact(telephone_book)
        elif action == 0:
            break
        else:
            print('Некорректно выбрано действие, попробуйте еще раз.\n')

choice()

