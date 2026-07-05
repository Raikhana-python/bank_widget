from src.widget import mask_account_card, get_date


class TestMaskAccountCard:
    """Тесты для функции mask_account_card."""

    def test_card_mask(self):
        """Тест маскировки карты."""
        result = mask_account_card("Visa Platinum 7000792289606361")
        assert result == "Visa Platinum 7000 79** **** 6361"

    def test_account_mask(self):
        """Тест маскировки счета."""
        result = mask_account_card("Счет 73654108430135874305")
        assert result == "Счет **4305"

    def test_invalid_empty_string(self):
        """Тест пустой строки."""
        result = mask_account_card("")
        assert "Ошибка" in result

    def test_invalid_format_no_number(self):
        """Тест строки без номера."""
        result = mask_account_card("Visa Platinum")
        assert "Ошибка" in result

    def test_invalid_wrong_length(self):
        """Тест номера с неправильной длиной."""
        result = mask_account_card("Card 12345")
        assert "Ошибка" in result


class TestGetDate:
    """Тесты для функции get_date."""

    def test_valid_date(self):
        """Тест корректной даты."""
        result = get_date("2024-03-11T02:26:18.671407")
        assert result == "11.03.2024"

    def test_another_valid_date(self):
        """Тест другой корректной даты."""
        result = get_date("2023-12-25T15:30:45.123456")
        assert result == "25.12.2023"

    def test_invalid_empty_string(self):
        """Тест пустой строки."""
        result = get_date("")
        assert "Ошибка" in result

    def test_invalid_format(self):
        """Тест неверного формата даты."""
        result = get_date("2023/12/25")
        assert "Ошибка" in result
