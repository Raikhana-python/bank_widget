"""Тесты для модуля processing."""

import pytest
from src.processing import filter_by_state, sort_by_date


class TestFilterByState:
    """Тесты для функции filter_by_state."""

    @pytest.mark.parametrize("state,expected_count", [
        ('EXECUTED', 2),
        ('CANCELED', 1),
        ('PENDING', 0),
    ])
    def test_filter_by_state(self, sample_operations, state, expected_count):
        """Тест фильтрации с параметризацией и фикстурой."""
        result = filter_by_state(sample_operations, state)
        assert len(result) == expected_count
        if expected_count > 0:
            assert all(item['state'] == state for item in result)

    def test_filter_default_state(self, sample_operations):
        """Тест фильтрации со значением по умолчанию."""
        result = filter_by_state(sample_operations)
        assert len(result) == 2
        assert all(item['state'] == 'EXECUTED' for item in result)

    def test_filter_empty_list(self):
        """Тест с пустым списком."""
        assert filter_by_state([]) == []


class TestSortByDate:
    """Тесты для функции sort_by_date."""

    def test_sort_descending(self, sample_operations):
        """Тест сортировки по убыванию."""
        result = sort_by_date(sample_operations)
        dates = [item['date'] for item in result]
        assert dates == sorted(dates, reverse=True)

    def test_sort_ascending(self, sample_operations):
        """Тест сортировки по возрастанию."""
        result = sort_by_date(sample_operations, descending=False)
        dates = [item['date'] for item in result]
        assert dates == sorted(dates)

    @pytest.mark.parametrize("descending,expected_order", [
        (True, ['2024-03-11T02:26:18.671407', '2024-03-09T10:15:30.987654']),
        (False, ['2024-03-09T10:15:30.987654', '2024-03-11T02:26:18.671407']),
    ])
    def test_sort_with_params(self, sample_operations, descending, expected_order):
        """Тест сортировки с параметризацией."""
        executed = [op for op in sample_operations if op['state'] == 'EXECUTED']
        result = sort_by_date(executed, descending=descending)
        dates = [item['date'] for item in result]
        assert dates == expected_order

    def test_sort_empty_list(self):
        """Тест с пустым списком."""
        assert sort_by_date([]) == []

    def test_sort_missing_date(self):
        """Тест с отсутствующей датой."""
        operations = [
            {'id': 1, 'date': '2024-03-11T10:00:00'},
            {'id': 2},
            {'id': 3, 'date': '2024-03-10T10:00:00'},
        ]
        result = sort_by_date(operations)
        assert result[0]['id'] == 1
        assert result[1]['id'] == 3
        assert result[2]['id'] == 2
