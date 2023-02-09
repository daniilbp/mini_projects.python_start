import os

# from collections.abc import Iterable
from typing import Iterable

def gen_files_path(user_path: str) -> Iterable[str]:
    for file in os.walk(os.path.abspath('/Skillbox'), topdown=True, onerror=None, followlinks=False):
        if file[0] == user_path:
            print('Указанный каталог найден!')
            return
        for file_path in file[2]:
            yield os.path.join(file[0], file_path)


path = os.path.abspath('../../../')
print(path)
catalogs = gen_files_path(path)
for i_catalog in catalogs:
    print(i_catalog)


# Traceback (most recent call last):
#   File "main.py", line 5, in <module>
#     def gen_files_path(user_path: str) -> Iterable[str]:
# TypeError: 'ABCMeta' object is not subscriptable
