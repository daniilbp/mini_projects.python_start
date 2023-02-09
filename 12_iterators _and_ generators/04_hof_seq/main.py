# from collections.abc import Iterable
from typing import Iterable

def q_hofstadter(lst: list) -> Iterable[int]:
    list_q_hofst = [0, 1, 1]
    if lst[1] == 2:
        raise StopIteration
    for n in range(1, lst[0] + 1):
        if n != 1 and n != 2:
            q = list_q_hofst[n - list_q_hofst[n - 1]] + list_q_hofst[n - list_q_hofst[n - 2]]
            list_q_hofst.append(q)
        yield list_q_hofst[n]

q_hofst = q_hofstadter([10, 1])
for i_q in q_hofst:
    print(i_q, end=' ')


# Traceback (most recent call last):
#   File "main.py", line 3, in <module>
#     def q_hofstadter(lst: list) -> Iterable[int]:
# TypeError: 'ABCMeta' object is not subscriptable

