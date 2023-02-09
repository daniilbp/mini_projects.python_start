from typing import Callable


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """ Декоратор, который даёт возможность любому декоратору принимать произвольные аргументы """
    def decorator_func(*args, **kwargs) -> Callable:
        def wrapper(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)
        return wrapper
    return decorator_func


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """ Декоратор, логирующий работу кода """
    def wrapped(*args, **kwargs) -> Callable:
        print(f'Переданные арги и кварги в декоратор: {dec_args} {dec_kwargs}')
        return func(*args, **kwargs)
    return wrapped


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print('Привет', text, num)


decorated_function('Юзер', 101)
