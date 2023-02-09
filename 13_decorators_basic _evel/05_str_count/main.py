from typing import Callable, Any


def counter(func: Callable) -> Callable:

    def wrapped_func(*args, **kwargs) -> Any:
        wrapped_func.count += 1
        res = func(*args, **kwargs)
        print(f'Функция {func.__name__} была вызвана {wrapped_func.count} раз(а)')
        return res
    wrapped_func.count = 0

    return wrapped_func


@counter
def hello():
    print('Hello!')


hello()
hello()
hello()
