import os

def size_catalog(path, c_f, c_p, c_s):
    for el in os.listdir(path):
        tmp_path = os.path.join(path, el)
        if os.path.isfile(tmp_path):
            c_f += 1
            c_s += os.path.getsize(tmp_path) / 1024
        else:
            c_p += 1
            c_f, c_p, c_s = size_catalog(tmp_path, c_f, c_p, c_s)

    return c_f, c_p, c_s

count_file, count_path, count_size = 0, 0, 0
path_from = os.path.abspath(os.path.join('..', '..', 'Module14'))

files, catalogs, size = size_catalog(path_from, count_file, count_path, count_size)

print(path_from)
print('Размер каталога (в Кб):', size)
print('Количество подкаталогов:', catalogs)
print('Количество файлов:', files)
