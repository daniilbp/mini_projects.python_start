# from collections.abc import Iterable
from typing import Iterable

def find_res(list_1: list, list_2: list, res: int) -> Iterable[tuple]:
    """
    Функция-генератор, генерирует числа из списков и их произведение.
    Выход из цикла происходит, если произведение равно 56
    """
    for x in list_1:
        for y in list_2:
            result = x * y
            # print(x, y, result)
            yield x, y, result
            if result == res:
                print('Found!!!')
                return

my_find = find_res([2, 5, 7, 10], [3, 8, 4, 9], 56)
for i_res in my_find:
    print(i_res)
