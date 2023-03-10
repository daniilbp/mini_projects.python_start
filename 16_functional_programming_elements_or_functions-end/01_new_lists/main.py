from typing import List
from functools import reduce


def calc(num_1: int, num_2: int) -> int:
    result = num_1 * num_2
    return result


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

print(list(map(lambda num: round(num ** 3, 3), floats)))
print(list(filter(lambda name: len(name) >= 5, names)))
print(reduce(calc, numbers))
