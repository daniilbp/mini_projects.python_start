def reader(text):
    with open(text, 'r') as file_from:
        data = file_from.read()

    return data


def frequency_analysis(str):
    uniq_lst, dct, alpha = [], {}, 'abcdefghijklmnopqrstuvwxyz'
    only_letter_str = ''.join([eng_letter for eng_letter in str if eng_letter in alpha])

    for el in only_letter_str:
        if el not in uniq_lst:
            uniq_lst.append(el)

    for sym in uniq_lst:
        if 1 / len(only_letter_str) * only_letter_str.count(sym) in dct:
            dct[1 / len(only_letter_str) * only_letter_str.count(sym)] = dct[1 / len(only_letter_str) * only_letter_str.count(sym)].union(set(sym))
        else:
            dct[1 / len(only_letter_str) * only_letter_str.count(sym)] = set(sym)

    return dct


def writer(info):
    with open('analysis.txt', 'w') as file_in:
        for share in sorted(info.keys())[::-1]:
            if isinstance(info[share], set):
                for letter in sorted(info[share]):
                    file_in.write(letter + ' {:.3f}\n'.format(share))
            else:
                file_in.write(info[share] + ' {:.3f}\n'.format(share))


text_from = reader('text.txt')

info_dct = frequency_analysis(text_from.lower())

writer(info_dct)
