import functools
from typing import Callable, Any


def check_permission(permission: str) -> Callable:
    """ Декоратор, который проверяет, есть ли у пользователя доступ к вызываемой функции """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Any:
            try:
                if permission not in user_permissions:
                    raise PermissionError
                return func(*args, **kwargs)
            except PermissionError:
                print(f'PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
        return wrapped
    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
