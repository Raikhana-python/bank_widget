"""Тесты для модуля widget."""

import pytest
from src.widget import mask_account_card, get_date


class TestMaskAccountCard:
    """Тесты для функции mask_account_card."""

    @pytest.mark.parametrize("input_data,expected", [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ])
    def test_valid_masks(self, input_data, expected):
        assert mask_account_card(input_data) == expected

    @pytest.mark.parametrize("input_data", [
        "",
        "Visa",
        "Счет",
    ])
    def test_invalid_input(self, input_data):
        result = mask_account_card(input_data)
        assert "Ошибка" in result

    def test_card_mask_with_fixture(self, sample_card_data):
        result = mask_account_card(sample_card_data["full_string"])
        assert result == f"Visa Platinum {sample_card_data['masked']}"

    def test_account_mask_with_fixture(self, sample_account_data):
        result = mask_account_card(sample_account_data["full_string"])
        assert result == f"Счет {sample_account_data['masked']}"


class TestGetDate:
    """Тесты для функции get_date."""

    @pytest.mark.parametrize("input_date,expected", [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-25T15:30:45.123456", "25.12.2023"),
        ("2025-01-01T00:00:00.000000", "01.01.2025"),
    ])
    def test_valid_dates(self, input_date, expected):
        assert get_date(input_date) == expected

    @pytest.mark.parametrize("input_date", [
        "",
        "2023/12/25",
        "invalid date",
    ])
    def test_invalid_dates(self, input_date):
        result = get_date(input_date)
        assert "Ошибка" in result

    def test_date_with_fixture(self, sample_date_string):
        assert get_date(sample_date_string) == "11.03.2024"
