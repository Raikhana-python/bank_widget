"""Тесты для модуля utils."""

import json

from src.utils import read_transactions_from_json


def test_read_from_existing_file(tmp_path):
    file_path = tmp_path / "test.json"
    data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f)

    result = read_transactions_from_json(str(file_path))
    assert result == data


def test_read_from_empty_file(tmp_path):
    file_path = tmp_path / "empty.json"
    file_path.touch()
    result = read_transactions_from_json(str(file_path))
    assert result == []


def test_read_from_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("not a json")
    result = read_transactions_from_json(str(file_path))
    assert result == []


def test_read_not_list(tmp_path):
    file_path = tmp_path / "not_list.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump({"key": "value"}, f)
    result = read_transactions_from_json(str(file_path))
    assert result == []


def test_file_not_found():
    result = read_transactions_from_json("non_existent.json")
    assert result == []
