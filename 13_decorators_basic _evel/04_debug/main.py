# import functools
from typing import Callable, Any


def debug(func: Callable) -> Callable:
    # @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:

        # lst_args = [f'\'{i_args}\'' if isinstance(i_args, str) else str(i_args) for i_args in args]
        # lst_kwargs = [f'{key}=\'{value}\'' if isinstance(value, str) else f'{key}={value}' for key, value in kwargs.items()]

        lst_args = [f'{repr(i_args)}' if isinstance(i_args, str) else str(i_args) for i_args in args]
        lst_kwargs = [f'{key}={repr(value)}' if isinstance(value, str) else f'{key}={value}' for key, value in kwargs.items()]

        print('Вызывается {func}({str})'.format(
            func=func.__name__, str=', '.join(lst_args + lst_kwargs)
        ))
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' вернула значение '{result}'")
        print(result, end='\n\n')

    return wrapped_func


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
