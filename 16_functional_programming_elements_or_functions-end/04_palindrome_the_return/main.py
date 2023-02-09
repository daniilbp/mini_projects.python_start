from collections import Counter


def can_be_poly(text: str) -> bool:
    return len(list(filter(lambda x: x % 2, Counter(text).values()))) <= 1


print(can_be_poly('abcba'))
print(can_be_poly('abbbcc'))
