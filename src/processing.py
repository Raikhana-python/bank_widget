"""Модуль для обработки данных о банковских операциях."""

from typing import Any, Dict, List


def filter_by_state(operations: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по значению ключа 'state'.

    Args:
        operations: Список словарей с данными операций.
        state: Значение для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
        Новый список словарей с операциями, у которых state совпадает с указанным.
    """
    if not operations:
        return []

    return [item for item in operations if item.get('state') == state]


def sort_by_date(operations: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате.

    Args:
        operations: Список словарей с данными операций.
        descending: Порядок сортировки. True - убывание, False - возрастание.

    Returns:
        Новый список словарей, отсортированный по дате.
    """
    if not operations:
        return []

    return sorted(operations, key=lambda x: x.get('date', ''), reverse=descending)
