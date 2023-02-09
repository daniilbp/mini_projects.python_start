# from collections.abc import Iterable, Iterator
from typing import Iterable, Iterator

class SquareNums:
    """ Базовый класс-итератор, генерирует последовательность из квадратов чисел """
    def __init__(self, num: int) -> None:
        self.count = 0
        self.num = num

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        self.count += 1
        if self.count > self.num:
            raise StopIteration
        return self.count ** 2


num = SquareNums(5)
for i_num in num:
    print(i_num, end=' ')


def square_num(num: int) -> Iterable[int]:
    """ Функция-генератор, генерирует последовательность из квадратов чисел """
    for elem in range(1, num+1):
        yield elem ** 2

print()
sq_num = square_num(5)
for i_value in sq_num:
    print(i_value, end=' ')


print() # генераторное выражение
square_gen = (i_el ** 2 for i_el in range(1, 6))
for elem in square_gen:
    print(elem, end=' ')


# Traceback (most recent call last):
#   File "main.py", line 3, in <module>
#     class SquareNums:
#   File "main.py", line 12, in SquareNums
#     def __next__(self) -> Iterator[int]:
# TypeError: 'ABCMeta' object is not subscriptable

