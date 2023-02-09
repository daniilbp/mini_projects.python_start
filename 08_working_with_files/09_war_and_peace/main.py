import zipfile

def frequency_analysis(zip_folder):
    dct = {}

    zip_from = zipfile.ZipFile(zip_folder, 'r')
    with open(zip_from.extract('voyna-i-mir.txt'), 'r', encoding='utf-8') as file_from:
        for line in file_from:
            for sym in line:
                if sym.isalpha():
                    if sym not in dct:
                        dct[sym] = 0
                    dct[sym] += 1

    zip_from.close()

    new_dct = {value: key for key, value in dct.items()}

    for el in sorted(new_dct.keys()):
        print(el, ' - ', new_dct[el])


frequency_analysis('voyna-i-mir.zip')
