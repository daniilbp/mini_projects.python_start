def origin(text):
    dict_text = dict()

    for letter in text:
        if letter in dict_text:
            dict_text[letter] += 1
        else:
            dict_text[letter] = 1

    print('Оригинальный словарь частот:')
    for i_info in sorted(dict_text.keys()):
        print(i_info, ':', dict_text[i_info])

    return dict_text

def inverted(input_dict):
    inverted_dict = dict()

    for key in input_dict:
        if input_dict[key] in inverted_dict:
            inverted_dict[input_dict[key]].append(key)
        else:
            inverted_dict[input_dict[key]] = [key]

    print('\nИнвертированный словарь частот:')
    for info in sorted(inverted_dict.keys()):
        print(info, ':', inverted_dict[info])

input_text = input('Введите текст: ')

origin_dict = origin(input_text)

inverted(origin_dict)
