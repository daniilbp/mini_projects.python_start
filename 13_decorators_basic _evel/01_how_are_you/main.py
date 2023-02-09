from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        func(*args, **kwargs)

    return wrapped_func

@how_are_you
def test() -> None:
    print('Hello!')


@how_are_you
def square_sum() -> None:
    num = 100
    res = sum([i_num ** 2 for i_num in range(1, num + 1)])
    print('Сумма квадратов чисел от 1 до {}: {}'.format(num, res))


test()
print()
square_sum()
