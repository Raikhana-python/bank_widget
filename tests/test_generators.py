"""Тесты для модуля generators."""

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


class TestFilterByCurrency:
    """Тесты для генератора filter_by_currency."""

    @pytest.fixture
    def sample_transactions(self):
        """Фикстура с тестовыми транзакциями."""
        return [
            {
                "id": 1,
                "description": "Перевод организации",
                "operationAmount": {"currency": {"code": "USD", "name": "USD"}},
            },
            {
                "id": 2,
                "description": "Перевод с карты на карту",
                "operationAmount": {"currency": {"code": "EUR", "name": "EUR"}},
            },
            {
                "id": 3,
                "description": "Покупка билетов",
                "operationAmount": {"currency": {"code": "USD", "name": "USD"}},
            },
        ]

    def test_filter_usd(self, sample_transactions):
        """Фильтрация по USD."""
        result = list(filter_by_currency(sample_transactions, "USD"))
        assert len(result) == 2
        assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)

    def test_filter_eur(self, sample_transactions):
        """Фильтрация по EUR."""
        result = list(filter_by_currency(sample_transactions, "EUR"))
        assert len(result) == 1
        assert result[0]["id"] == 2

    def test_filter_no_match(self, sample_transactions):
        """Нет транзакций с такой валютой."""
        result = list(filter_by_currency(sample_transactions, "RUB"))
        assert result == []

    def test_empty_list(self):
        """Пустой список транзакций."""
        result = list(filter_by_currency([], "USD"))
        assert result == []


class TestTransactionDescriptions:
    """Тесты для генератора transaction_descriptions."""

    @pytest.fixture
    def sample_transactions(self):
        """Фикстура с транзакциями."""
        return [
            {"id": 1, "description": "Перевод организации"},
            {"id": 2, "description": "Перевод с карты на карту"},
            {"id": 3, "description": "Покупка билетов"},
        ]

    def test_descriptions(self, sample_transactions):
        """Проверка получения описаний."""
        result = list(transaction_descriptions(sample_transactions))
        expected = ["Перевод организации", "Перевод с карты на карту", "Покупка билетов"]
        assert result == expected

    def test_missing_description(self):
        """Транзакция без описания."""
        transactions = [{"id": 1}]
        result = list(transaction_descriptions(transactions))
        assert result == [""]

    def test_empty_list(self):
        """Пустой список."""
        result = list(transaction_descriptions([]))
        assert result == []


class TestCardNumberGenerator:
    """Тесты для генератора card_number_generator."""

    @pytest.mark.parametrize("start,end,expected", [
        (1, 1, ["0000 0000 0000 0001"]),
        (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
        (99999999, 100000000, ["0000 0000 9999 9999", "0000 0001 0000 0000"]),
    ])
    def test_card_numbers(self, start, end, expected):
        """Тест генерации номеров карт с параметризацией."""
        result = list(card_number_generator(start, end))
        assert result == expected

    def test_single_number(self):
        """Генерация одного номера."""
        gen = card_number_generator(1, 1)
        assert next(gen) == "0000 0000 0000 0001"

    def test_range_length(self):
        """Проверка количества сгенерированных номеров."""
        gen = card_number_generator(10, 15)
        result = list(gen)
        assert len(result) == 6
        assert result[0] == "0000 0000 0000 0010"
        assert result[-1] == "0000 0000 0000 0015"
