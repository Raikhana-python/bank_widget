"""Модуль с генераторами для обработки транзакций."""

from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Генератор, который поочерёдно выдаёт транзакции с заданной валютой.

    Args:
        transactions: Список словарей с данными транзакций.
        currency: Код валюты (например, 'USD').

    Yields:
        Словарь транзакции, если валюта совпадает.

    Examples:
        >>> transactions = [
        ...     {'id': 1, 'operationAmount': {'currency': {'code': 'USD'}}},
        ...     {'id': 2, 'operationAmount': {'currency': {'code': 'EUR'}}},
        ... ]
        >>> for t in filter_by_currency(transactions, 'USD'):
        ...     print(t['id'])
        1
    """
    for transaction in transactions:
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор, который возвращает описание каждой транзакции по очереди.

    Args:
        transactions: Список словарей с транзакциями.

    Yields:
        Описание транзакции (строка).

    Examples:
        >>> transactions = [
        ...     {'description': 'Перевод организации'},
        ...     {'description': 'Покупка билетов'},
        ... ]
        >>> for desc in transaction_descriptions(transactions):
        ...     print(desc)
        Перевод организации
        Покупка билетов
    """
    for transaction in transactions:
        yield transaction.get('description', '')


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор, который выдаёт номера карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start: Начальное значение (включительно).
        end: Конечное значение (включительно).

    Yields:
        Номер карты в формате 'XXXX XXXX XXXX XXXX'.

    Examples:
        >>> gen = card_number_generator(1, 3)
        >>> next(gen)
        '0000 0000 0000 0001'
        >>> next(gen)
        '0000 0000 0000 0002'
        >>> next(gen)
        '0000 0000 0000 0003'
    """
    for num in range(start, end + 1):
        # Форматируем число как 16-значное с ведущими нулями
        card_str = f"{num:016d}"
        # Разбиваем на группы по 4 цифры
        yield " ".join(card_str[i:i+4] for i in range(0, 16, 4))
