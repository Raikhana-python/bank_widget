"""Общие фикстуры для тестов."""

import pytest


@pytest.fixture
def sample_operations():
    """Фикстура с тестовыми данными операций."""
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2024-03-11T02:26:18.671407",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
            "from": "Visa Gold 8326537236217879",
            "to": "Счет 38573808354569585904"
        },
        {
            "id": 413875756,
            "state": "CANCELED",
            "date": "2024-03-10T14:30:12.123456",
            "operationAmount": {
                "amount": "12500.00",
                "currency": {"name": "RUB", "code": "RUB"}
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831962478616213",
            "to": "Visa Gold 5999413478420683"
        },
        {
            "id": 587985671,
            "state": "EXECUTED",
            "date": "2024-03-09T10:15:30.987654",
            "operationAmount": {
                "amount": "876.50",
                "currency": {"name": "EUR", "code": "EUR"}
            },
            "description": "Покупка билетов",
            "to": "Счет 73654108430135874305"
        }
    ]


@pytest.fixture
def sample_card_data():
    """Фикстура с тестовыми данными карты."""
    return {
        "card_number": "7000792289606361",
        "masked": "7000 79** **** 6361",
        "full_string": "Visa Platinum 7000792289606361"
    }


@pytest.fixture
def sample_account_data():
    """Фикстура с тестовыми данными счета."""
    return {
        "account_number": "73654108430135874305",
        "masked": "**4305",
        "full_string": "Счет 73654108430135874305"
    }


@pytest.fixture
def sample_date_string():
    """Фикстура с тестовой датой."""
    return "2024-03-11T02:26:18.671407"
