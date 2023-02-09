import time
import datetime
from typing import Callable, Any
# from datetime import datetime


def logging(cls, func: Callable, date_format: str) -> Callable:
    """ Декоратор, логирующий работу кода """
    format = date_format.split()
    def wrapped(*args, **kwargs) -> Any:
        # format = date_format
        # for sym in format:
        #     if sym.isalpha():
        #         format = format.replace(sym, '%' + sym)
        #
        # print(f"Запускается '{cls.__name__}.{func.__name__}'. Дата и время запуска: {datetime.now().strftime(format)}")

        str_b = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        new_format = []
        dt = str(datetime.datetime.now())
        sym_list = {'Y': dt[:4], 'd': dt[8:10], 'b': str_b[int(dt[5:7]) - 1], 'H': dt[11:13], 'M': dt[14:16],
                    'S': dt[17:19], 'H:M:S': dt[11:19]}
        for i_el in format:
            if i_el in sym_list:
                new_format.append(sym_list[i_el])
            else:
                new_format.append(i_el)
        new_format = ' '.join(new_format)
        print(f'Запускается \'{cls.__name__}.{func.__name__}\'. Дата и время запуска: {new_format}')
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Завершение \'{cls.__name__}.{func.__name__}\', время работы = {round(time.time() - start, 3)}s')
        return result

    return wrapped


def log_methods(format: str) -> Callable:
    """
    Декоратор класса, который логирует все методы класса (кроме магических методов)
    и в который можно передавать формат вывода даты и времени логирования.
    """
    def decorate(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                cur_method = getattr(cls, i_method)
                decorated_method = logging(cls, cur_method, format)
                setattr(cls, i_method, decorated_method)

        return cls

    return decorate


@log_methods('b d Y - H:M:S')
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods('b d Y - H:M:S')
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
