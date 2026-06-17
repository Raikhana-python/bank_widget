"""Модуль с основными функциями для работы с банковскими картами и счетами."""

from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_info: str) -> str:
    """
    Маскирует номер карты или счета в строке с информацией.

    Args:
        card_info (str): Строка с типом и номером карты или счета.
            Примеры:
                - "Visa Platinum 7000792289606361"
                - "Maestro 7000792289606361"
                - "Счет 73654108430135874305"

    Returns:
        str: Строка с замаскированным номером.
            Для карт: "Visa Platinum 7000 79** **** 6361"
            Для счетов: "Счет **4305"

    Examples:
        >>> mask_account_card("Visa Platinum 7000792289606361")
        'Visa Platinum 7000 79** **** 6361'

        >>> mask_account_card("Счет 73654108430135874305")
        'Счет **4305'
    """
    if not card_info or not isinstance(card_info, str):
        return "Ошибка: пустая строка или неверный тип данных"

    parts = card_info.split()

    if len(parts) < 2:
        return "Ошибка: некорректный формат ввода"

    number = parts[-1]

    if not number.isdigit():
        return "Ошибка: номер должен содержать только цифры"

    if len(number) == 16:
        masked_number = get_mask_card_number(number)
    elif len(number) == 20:
        masked_number = get_mask_account(number)
    else:
        return f"Ошибка: номер должен содержать 16 или 20 цифр (получено {len(number)})"

    return " ".join(parts[:-1] + [masked_number])


def get_date(date_string: str) -> str:
    """
    Преобразует дату из ISO-формата в формат ДД.ММ.ГГГГ.

    Args:
        date_string (str): Строка с датой в формате ISO.
            Пример: "2024-03-11T02:26:18.671407"

    Returns:
        str: Дата в формате "ДД.ММ.ГГГГ".
            Пример: "11.03.2024"

    Examples:
        >>> get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'

        >>> get_date("2023-12-25T15:30:45.123456")
        '25.12.2023'
    """
    if not date_string or not isinstance(date_string, str):
        return "Ошибка: пустая строка или неверный тип данных"

    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Ошибка: некорректный формат даты"
