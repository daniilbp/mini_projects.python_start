from typing import Callable, Any
import time


def sleep(func: Callable, timeout=5) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        time.sleep(timeout)
        res = func(*args, **kwargs)

        return res

    return wrapped_func

@sleep
def big_func(number: int) -> int:
    result = sum([el ** 4 for _ in range(number + 1) for el in range(10000)])

    return result


print(big_func(300))
