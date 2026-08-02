"""Тесты для модуля external_api."""

import os
from unittest.mock import MagicMock, patch

import pytest

from src.external_api import convert_currency


@patch('src.external_api.requests.get')
def test_convert_rub(mock_get, monkeypatch):
    """Конвертация RUB (без вызова API)."""
    transaction = {
        'operationAmount': {
            'amount': '100.50',
            'currency': {'code': 'RUB'}
        }
    }
    result = convert_currency(transaction)
    assert result == 100.50
    mock_get.assert_not_called()


@patch('src.external_api.requests.get')
def test_convert_usd_success(mock_get, monkeypatch):
    """Успешная конвертация USD -> RUB."""
    monkeypatch.setenv('EXCHANGE_RATES_API_KEY', 'fake_key')
    transaction = {
        'operationAmount': {
            'amount': '10',
            'currency': {'code': 'USD'}
        }
    }
    mock_response = MagicMock()
    mock_response.json.return_value = {'success': True, 'result': 750.0}
    mock_response.raise_for_status = MagicMock()
    mock_get.return_value = mock_response

    result = convert_currency(transaction)
    assert result == 750.0
    mock_get.assert_called_once()


@patch('src.external_api.requests.get')
def test_convert_api_error(mock_get, monkeypatch):
    """Ошибка API."""
    monkeypatch.setenv('EXCHANGE_RATES_API_KEY', 'fake_key')
    transaction = {
        'operationAmount': {
            'amount': '10',
            'currency': {'code': 'USD'}
        }
    }
    mock_response = MagicMock()
    mock_response.json.return_value = {'success': False}
    mock_response.raise_for_status = MagicMock()
    mock_get.return_value = mock_response

    result = convert_currency(transaction)
    assert result == 0.0


@patch('src.external_api.requests.get')
def test_convert_no_api_key(mock_get, monkeypatch):
    """Отсутствие API-ключа."""
    monkeypatch.delenv('EXCHANGE_RATES_API_KEY', raising=False)
    transaction = {
        'operationAmount': {
            'amount': '10',
            'currency': {'code': 'USD'}
        }
    }
    result = convert_currency(transaction)
    assert result == 0.0
    mock_get.assert_not_called()


def test_convert_missing_fields():
    """Отсутствие полей amount или currency."""
    transaction = {'operationAmount': {}}
    result = convert_currency(transaction)
    assert result == 0.0
