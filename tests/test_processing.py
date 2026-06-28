"""Тесты для модуля processing."""

from src.processing import filter_by_state, sort_by_date


class TestFilterByState:
    """Тесты для функции filter_by_state."""

    def test_filter_executed_default(self):
        operations = [
            {'id': 1, 'state': 'EXECUTED'},
            {'id': 2, 'state': 'CANCELED'},
            {'id': 3, 'state': 'EXECUTED'},
        ]
        result = filter_by_state(operations)
        assert len(result) == 2
        assert all(item['state'] == 'EXECUTED' for item in result)

    def test_filter_canceled(self):
        operations = [
            {'id': 1, 'state': 'EXECUTED'},
            {'id': 2, 'state': 'CANCELED'},
            {'id': 3, 'state': 'CANCELED'},
        ]
        result = filter_by_state(operations, 'CANCELED')
        assert len(result) == 2
        assert all(item['state'] == 'CANCELED' for item in result)

    def test_filter_empty_list(self):
        result = filter_by_state([])
        assert result == []


class TestSortByDate:
    """Тесты для функции sort_by_date."""

    def test_sort_descending_default(self):
        operations = [
            {'id': 1, 'date': '2024-03-10T10:00:00'},
            {'id': 2, 'date': '2024-03-12T10:00:00'},
            {'id': 3, 'date': '2024-03-11T10:00:00'},
        ]
        result = sort_by_date(operations)
        assert result[0]['id'] == 2
        assert result[1]['id'] == 3
        assert result[2]['id'] == 1

    def test_sort_ascending(self):
        operations = [
            {'id': 1, 'date': '2024-03-10T10:00:00'},
            {'id': 2, 'date': '2024-03-12T10:00:00'},
            {'id': 3, 'date': '2024-03-11T10:00:00'},
        ]
        result = sort_by_date(operations, descending=False)
        assert result[0]['id'] == 1
        assert result[1]['id'] == 3
        assert result[2]['id'] == 2

    def test_sort_empty_list(self):
        result = sort_by_date([])
        assert result == []


