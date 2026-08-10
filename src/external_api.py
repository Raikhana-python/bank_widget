"""Функции для работы с внешними API."""

import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_currency(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными транзакции.

    Returns:
        Сумма в рублях (float). Если валюта уже RUB, возвращает сумму без изменений.
        Если валюта USD/EUR — выполняет запрос к API и конвертирует.
        В случае ошибки возвращает 0.0.
    """
    amount = transaction.get('operationAmount', {}).get('amount')
    currency = transaction.get('operationAmount', {}).get('currency', {}).get('code')
    if amount is None or currency is None:
        return 0.0

    if currency == 'RUB':
        return float(amount)

    api_key = os.getenv('EXCHANGE_RATES_API_KEY')
    if not api_key:
        return 0.0

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": api_key}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get('success'):
            return data.get('result', 0.0)
        else:
            return 0.0
    except (requests.RequestException, ValueError):
        return 0.0
