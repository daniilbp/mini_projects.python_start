from typing import Callable, Any


app = {}


def callback(param: str) -> Callable:
    def wrapper(func: Callable) -> Callable:
        app[param] = func
        def wrapped(*args, **kwargs) -> Any:
            return func(*args, **kwargs)
        return wrapped
    return wrapper


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
