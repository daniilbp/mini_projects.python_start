import os

# from collections.abc import Iterable
from typing import Iterable

def str_count(user_path: str) -> Iterable[int]:
    for info in os.walk(user_path, topdown=True, onerror=None, followlinks=False):
        print(info)
        for file in info[2]:
            if file.endswith('.py'):
                print(os.path.join(info[0], file))
                with open(os.path.join(info[0], file), 'r', encoding='utf-8') as file_2:
                    for line in file_2:
                        if (not line.startswith('\n')) and (not line.lstrip().startswith('#')):
                            yield 1


print(sum(str_count(os.path.abspath('../'))))


# Traceback (most recent call last):
#   File "main.py", line 5, in <module>
#     def str_count(user_path: str) -> Iterable[int]:
# TypeError: 'ABCMeta' object is not subscriptable

