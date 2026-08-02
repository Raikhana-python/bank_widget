"""Утилиты для работы с данными транзакций."""

import json
from typing import Any, Dict, List


def read_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает транзакции из JSON-файла и возвращает список словарей.

    Args:
        file_path: Путь к JSON-файлу.

    Returns:
        Список словарей с транзакциями. Если файл не найден, пуст или содержит не список — возвращает пустой список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        return []
