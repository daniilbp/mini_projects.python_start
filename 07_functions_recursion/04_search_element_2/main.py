site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def quest_fun():
    quest = input('Хотите ввести максимальную глубину? Y/N: ').lower()
    if quest == 'y':
        deep = int(input('Введите максимальную глубину: '))
        if 3 < deep or deep <= 0:
            print('Некорректная глубина. Введите глубину от 1 до 3.')
            quest_fun()
    elif quest == 'n':
        deep = 3
    else:
        print('Некорректный ввод. Введите Y/N.')
        quest_fun()

    return deep

def find_key(struct, key, lvl, count):
    result = None

    if count == lvl:
        return result
    count += 1

    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, lvl, count)
            if result:
                break

    return result

user_key = input('Введите искомый ключ: ')
answer = quest_fun()
result = find_key(site, user_key, answer, 0)
print('Значение ключа:', result)
