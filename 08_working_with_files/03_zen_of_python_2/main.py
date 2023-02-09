import os

def counter():
    count_str, count_word, count_letter, dct_alpha = 1, 1, 0, {}
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    with open(os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt')), 'r') as file_from:
        data = file_from.read().lower()

    for sym in data:
        if sym == '\n':
            count_str += 1
        if sym == ' ' or sym == '\n':
            count_word += 1
        else:
            count_letter += 1

        if sym in dct_alpha and sym in alpha:
            dct_alpha[sym] += 1
        elif sym not in dct_alpha and sym in alpha:
            dct_alpha[sym] = 1

    print('Количество букв в файле:', count_letter)
    print('Количество слов в файле:', count_word)
    print('Количество строк в файле:', count_str)

    num_rare_letter = min(dct_alpha.values())
    for letter_dct, num_letter in dct_alpha.items():
        if num_letter == num_rare_letter:
            print('Наиболее редкая буква:', letter_dct)
            break

counter()
