"""Модуль с декоратором для логирования вызовов функций."""

import functools
import os
import sys
from datetime import datetime
from typing import Any, Callable, Optional, TypeVar, cast

F = TypeVar('F', bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор для логирования вызовов функций.

    Args:
        filename: Имя файла для записи логов. Если None — логи выводятся в консоль.

    Returns:
        Декорированная функция.
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            func_name = func.__name__
            args_repr = ", ".join([repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()])
            log_message = f"{time_str} - {func_name}({args_repr})"

            try:
                result = func(*args, **kwargs)
                full_log = f"{log_message} -> {repr(result)}\n"
                _write_log(full_log, filename)
                return result
            except Exception as e:
                error_log = f"{log_message} -> ERROR: {type(e).__name__}: {e}\n"
                _write_log(error_log, filename)
                raise

        return cast(F, wrapper)
    return decorator


def _write_log(message: str, filename: Optional[str] = None) -> None:
    """Записывает сообщение в файл или выводит в консоль."""
    if filename:
        os.makedirs(os.path.dirname(os.path.abspath(filename)) or '.', exist_ok=True)
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(message)
    else:
        sys.stderr.write(message)
