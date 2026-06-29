"""Тесты для функций маскировки."""

import pytest
from src.masks import get_mask_card_number, get_mask_account


class TestMaskCardNumber:
    """Тесты для маскировки номера карты."""

    @pytest.mark.parametrize("card_number,expected", [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("0000000000000000", "0000 00** **** 0000"),
    ])
    def test_valid_card(self, card_number, expected):
        assert get_mask_card_number(card_number) == expected

    @pytest.mark.parametrize("card_number", [
        "",
        "1234",
        "123456789012345",
        "12345678901234567",
    ])
    def test_invalid_card(self, card_number):
        assert get_mask_card_number(card_number) == "Неверный номер карты"


class TestMaskAccount:
    """Тесты для маскировки номера счета."""

    @pytest.mark.parametrize("account_number,expected", [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
        ("00000000000000000000", "**0000"),
    ])
    def test_valid_account(self, account_number, expected):
        assert get_mask_account(account_number) == expected

    @pytest.mark.parametrize("account_number", [
        "",
        "123",
        "12",
    ])
    def test_invalid_account(self, account_number):
        assert get_mask_account(account_number) == "Неверный номер счета"
