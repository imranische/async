from asyncio import Task
from typing import Callable, Coroutine, Any
import asyncio


async def f(x):
    y = x ** 2
    print(y)
    return y


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    # На вход приходит одна из стадий жизненного цикла корутины, необходимо вернуть результат
    # её выполнения.

    if isinstance(f, Callable):
        y = asyncio.create_task(f(1))
    elif isinstance(f, Task):
        y = asyncio.create_task(f(2))
    elif isinstance(f, Coroutine):
        y = asyncio.create_task(f(3))
    else:
        raise ValueError('invalid argument')
    await y

if __name__ == '__main__':
    asyncio.run(await_my_func(f))
