"""Общие фикстуры для тестов."""
import pytest


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
