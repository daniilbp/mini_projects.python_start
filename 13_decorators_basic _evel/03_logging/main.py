import datetime
from typing import Callable,Any


def logging(func: Callable) ->Callable:
    """ Декоратор, логирующий работу кода """

    def wrapped_func(*args, **kwargs) -> Any:
        print('\nВызов функции {func}\t'
              'Позиционные аргументы: {args}\t'
              'Именованные аргументы: {kwargs}\n'
              '{doc}'.format(
            func=func.__name__, args=args, kwargs=kwargs, doc=func.__doc__
        ))
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            dt_error = datetime.datetime.now()
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                file.write(f'Функция: {func.__name__}\tОшибка {type(exc)}: {exc}\tДата и время ошибки: {dt_error}\n')
            print('Ошибка записана в файл function_errors.log')
        else:
            print('Фунцкия успешно завершила работу')
            return result

    return wrapped_func


@logging
def square_sum_1() -> int:
    """
    Функция наждения суммы квадратов
    от 0 до N,
    где 0 <= N <= 100
    :return: сумма квадратов
    """
    num = 'a'
    res = sum([i_num ** 2 for i_num in range(1, num + 1)])

    return res


@logging
def square_sum_2() -> int:
    """
    Функция наждения суммы квадратов
    от 0 до N,
    где 0 <= N <= 100
    :return: сумма квадратов
    """
    num = 100
    res = sum([i_num ** 2 for i_num in range(1, num + 1)])

    return res


@logging
def square_sum_3() -> int:
    """
    Функция наждения квадратов в список
    от 0 до N,
    где 0 <= N <= 100
    :return: сумма квадратов
    """
    num = 100
    res = [i_num ** 2 for i_num in range(1, num + 1)]

    return res[1000]


@logging
def square_sum_4() -> int:
    """
    Функция наждения суммы квадратов
    от 0 до N,
    где 0 <= N <= 10
    :return: сумма квадратов
    """
    num = 10
    res = sum([i_num ** 2 for i_num in range(1, num + 1)])

    return res


square_sum_1()
square_sum_2()
square_sum_3()
square_sum_4()
